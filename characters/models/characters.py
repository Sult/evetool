import time
from collections import OrderedDict
from datetime import datetime, timedelta

from django.db import models
from django.conf import settings
from django.utils.timezone import utc

from .skills import Skill, SkillGroup
from metrics.models import Corporation
from tasks.models import EveApiCache, Task
from evetool.storage import OverwriteStorage

import utils


class CharacterApi(models.Model):
    """ charactertype apis """

    api = models.ForeignKey("apis.Api")
    characterid = models.BigIntegerField()
    charactername = models.CharField(max_length=254)
    corporationid = models.BigIntegerField()
    corporationname = models.CharField(max_length=254)

    def __unicode__(self):
        return self.charactername

    #get right icon for characters view
    def view_icon(self):
        try:
            icon = self.characterapiicon_set.get(size=128, relation=self)
            return icon.icon
        except CharacterApiIcon.DoesNotExist:
            return None

    #def character sheet image
    def sheet_icon(self):
        try:
            icon = self.characterapiicon_set.get(size=200, relation=self)
            return icon.icon
        except CharacterApiIcon.DoesNotExist:
            return None

    def current_balance(self):
        if self.api.access_to("CharacterInfo"):
            sheet = utils.connection.api_request(
                "CharacterInfoAuth", obj=self
            )
            if sheet.accountBalance:
                return round(float(sheet.accountBalance), 2)
        return 0

    def sheet_cache_key(self):
        key = "CharacterInfo"
        category = EveApiCache.EVE
        kwargs = {"characterID": self.characterid}
        if self.api.access_to("CharacterInfo"):
            return utils.connection.generate_cache_key(
                category, key, api=self.api, **kwargs
            )
        else:
            return utils.connection.generate_cache_key(category, key)

    def sheet_set_cache_job(self):
        key = "CharacterInfo"
        category = EveApiCache.EVE
        kwargs = {"characterID": self.characterid}
        if self.api.access_to("CharacterInfo"):
            api = self.api
        else:
            api = None

        EveApiCache.objects.create(
            priority=Task.VERY_HIGH,
            api=api,
            category=category,
            key=key,
            kwargs=kwargs,
        )

    #get the data for landing page after character selection
    def character_sheet(self):
        sheet = utils.connection.get_cache(self.sheet_cache_key())
        employment = self.employment_history(sheet)
        return sheet, employment

    #employment history of a player
    @staticmethod
    def employment_history(sheet):
        cache_key = "employment_history_%d" % int(sheet.characterID)
        #result = utils.connection.get_cache(cache_key)
        result = None
        if not result:
            cache_timer = 60 * 60
            result = []
            for corp_data in sheet.employmentHistory:
                result.append({
                    "corporation": Corporation.find_corporation(
                        corp_data.corporationID
                    ),
                    "startdate": utils.common.convert_timestamp(
                        corp_data.startDate
                    )
                })
            utils.connection.set_cache(cache_key, result, cache_timer)
        return result

    #get skill in training
    def skill_in_training(self):
        training_skill = None
        if self.api.access_to("SkillInTraining"):
            in_training = utils.connection.api_request(
                "SkillInTraining", obj=self
            )
            try:
                training_skill = {
                    "skill": Skill.objects.get(
                        typeid=int(in_training.trainingTypeID)
                    ).typename,
                    "to_level": int(in_training.trainingToLevel),
                    "finnished": utils.common.convert_timestamp(
                        in_training.trainingEndTime
                    )
                }
            except AttributeError:
                training_skill = {"skill": "No skill in training"}
        return training_skill

    #characters trained skills
    def trained_skills(self):
        cache_key = "trained_skills_%d" % self.pk
        result = utils.connection.get_cache(cache_key)
        if not result:
            cache_timer = 60 * 5
            sheet = utils.connection.api_request("CharacterSheet", obj=self)
            groups = SkillGroup.objects.exclude(
                groupname="Fake Skills"
            ).order_by("groupname")
            skills = Skill.objects.order_by("typename")
            all_skills = OrderedDict()
            skillpoints = {}

            for group in groups:
                all_skills[group.groupname] = list()
                skillpoints[group.groupname] = 0

            for skill in skills:
                trained = sheet.skills.Get(skill.typeid, False)
                if trained:
                    all_skills[skill.skillgroup.groupname].append(
                        {
                            "skill": skill,
                            "level": int(trained.level)
                        }
                    )
                    skillpoints[skill.skillgroup.groupname] += \
                        trained.skillpoints

            result = {
                "all_skills": all_skills,
                "skillpoints": skillpoints,
            }

            utils.connection.set_cache(cache_key, result, cache_timer)
        return result

    #get skillqueue
    def skill_queue(self):
        queue = None
        if self.api.access_to("SkillQueue"):
            queue = {}

            skills = utils.connection.api_request(
                "SkillQueue", obj=self
            ).skillqueue
            queue["skills"] = skills
            queue["total"] = self.total_skillpoints(skills)
            now = datetime.now().replace(tzinfo=utc)
            try:
                trainingtime = utils.common.convert_timestamp(
                    skills[-1].endTime
                ) - now
                trainingtime -= timedelta(
                    microseconds=trainingtime.microseconds
                )
                queue["trainingtime"] = trainingtime
            except TypeError:
                pass
        return queue

    #get total skillpoints for skills in queue
    @staticmethod
    def total_skillpoints(skills):
        total = 0
        for skill in skills:
            total += int(skill.endSP - skill.startSP)
        return total

    #walletjournal
    def wallet_journal(self):
        cache_key = "walletjournal_character_%d" % self.pk
        result = utils.connection.get_cache(cache_key)
        if not result:
            self.update_journal()
            cache_timer = 60 * 10
            utils.connection.set_cache(cache_key, True, cache_timer)
        return CharacterJournal.objects.filter(characterapi=self)

    #updates journal to current moment
    def update_journal(self):
        fromid = 0
        transactions = utils.connection.api_request(
            "WalletJournal", obj=self, rowcount=2500
        ).transactions

        while True:
            for trans in transactions:
                date = utils.common.convert_timestamp(trans.date)
                #check for duplicate
                if CharacterJournal.objects.filter(
                    characterapi=self,
                    balance=trans.balance,
                    date=date,
                ).exists():
                    continue
                else:
                    CharacterJournal.create_entry(self, trans)

                    if int(trans.refID) < fromid or fromid == 0:
                        fromid = int(trans.refID)
            if len(transactions) < 2500:
                break
            else:
                time.sleep(1)
                transactions = utils.connection.api_request(
                    "WalletJournal", obj=self, rowcount=2500, fromid=fromid
                ).transactions


class CharacterApiIcon(models.Model):
    """ images related to characters """

    relation = models.ForeignKey("characters.CharacterApi")
    size = models.IntegerField(choices=settings.IMAGE_SIZES)
    typeid = models.IntegerField()
    icon = models.ImageField(
        upload_to="images/characters/",
        storage=OverwriteStorage(),
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ["size", "relation"]

    def __unicode__(self):
        return "Character Image %s" % self.relation.charactername

    # def save(self, *args, **kwargs):
    #     try:
    #         temp = CharacterApiIcon.objects.get(pk=self.pk)
    #         if temp.icon != self.icon:
    #             temp.icon.delete()
    #     except ObjectDoesNotExist:
    #         pass
    #     super(CharacterApiIcon, self).save(*args, **kwargs)

    #get list of wanted character icon sizes
    @staticmethod
    def icon_sizes():
        return [128, 200]


class Transaction(models.Model):

    reftypeid = models.SmallIntegerField()
    ownername1 = models.CharField(max_length=254)
    ownerid1 = models.IntegerField()
    ownername2 = models.CharField(max_length=254)
    ownerid2 = models.IntegerField()
    argname1 = models.CharField(max_length=254)
    argid1 = models.IntegerField()
    amount = models.FloatField(null=True)
    reason = models.TextField(blank=True)
    taxreceiverid = models.IntegerField(null=True)
    taxamount = models.FloatField(null=True)

    class Meta:
        abstract = True


class CharacterJournal(Transaction):
    """
    Wallet transcations of a player. Saved to database so data can
    be filtered, and metadata can be created.
    Like balance graphs, see how much you paid in taxes and more.
    """

    characterapi = models.ForeignKey(CharacterApi)
    date = models.DateTimeField()
    balance = models.FloatField()

    class Meta:
        unique_together = ["characterapi", "date", "balance"]
        ordering = ["-date", "-reftypeid"]

    def __unicode__(self):
        return "%s's transaction" % self.characterapi.charactername

    @staticmethod
    def create_entry(characterapi, transaction):
        if transaction.taxReceiverID == "":
            taxreceiverid = None
        else:
            taxreceiverid = int(transaction.taxReceiverID)

        if transaction.taxAmount == "":
            taxamount = None
        else:
            taxamount = round(float(transaction.taxAmount), 2)

        date = utils.common.convert_timestamp(transaction.date)
        CharacterJournal.objects.create(
            characterapi=characterapi,
            date=date,
            balance=round(float(transaction.balance), 2),
            reftypeid=int(transaction.refTypeID),
            ownername1=str(transaction.ownerName1),
            ownerid1=int(transaction.ownerID1),
            ownername2=str(transaction.ownerName2),
            ownerid2=int(transaction.ownerID2),
            argname1=str(transaction.argName1),
            argid1=int(transaction.argID1),
            amount=round(float(transaction.amount), 2),
            reason=str(transaction.reason),
            taxreceiverid=taxreceiverid,
            taxamount=taxamount,
        )

    @staticmethod
    def monthly_balance(characterapi):
        last_restart = utils.common.last_server_restart()
        days = last_restart - timedelta(days=31)
        entries = CharacterJournal.objects.filter(
            characterapi=characterapi,
            date__range=[days, last_restart]
        )

        balance = []
        for days in range(31):
            first = entries.first()
            date = (last_restart - timedelta(days=days))
            #make timestamp in miliseconds
            timestamp = int(time.mktime(date.timetuple()) * 1000)
            if first:
                isk = first.balance
            else:
                try:
                    isk = balance[-1][1]
                except IndexError:
                    isk = characterapi.current_balance()

            balance.append([timestamp, isk])
            entries = entries.filter(date__lt=(date - timedelta(days=1)))
        #return reversed list
        return balance[::-1]

    @staticmethod
    def weekly_balance(characterapi):
        now = datetime.now().replace(tzinfo=utc)
        entries = CharacterJournal.objects.filter(
            characterapi=characterapi,
            date__range=[
                now.replace(hour=23, minute=59, second=0) - timedelta(days=9),
                now
            ]
        )

        balance = []
        for days in range(8):
            date = now.replace(
                hour=0, minute=0, second=0
            ) - timedelta(days=days)

            day_entries = entries.filter(
                date__lt=now.replace(
                    hour=23, minute=59, second=59
                ) - timedelta(days=days),
                date__gt=date
            )
            if not day_entries.count() > 0:
                try:
                    isk = balance[-1][1]
                except IndexError:
                    isk = characterapi.current_balance()
                timestamp = int(time.mktime(date.timetuple()) * 1000)
                balance.append([timestamp, isk])

            else:
                for entry in day_entries:
                    timestamp = int(time.mktime(entry.date.timetuple()) * 1000)
                    balance.append([timestamp, entry.balance])

        #add last value for date on xaxis
        date = now.replace(hour=23, minute=59, second=59) - timedelta(days=8)
        isk = balance[-1][1]
        timestamp = int(time.mktime(date.timetuple()) * 1000)
        balance.append([timestamp, isk])
        return balance[::-1]
