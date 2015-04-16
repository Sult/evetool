from datetime import datetime
import time

from django.utils.timezone import utc
import eveapi

from apps.bulk.models import AllianceBulk, CorporationBulk


def get_date_from_stamp(stamp):
    try:
        temp = datetime.fromtimestamp(stamp).replace(tzinfo=utc)
        return temp
    except TypeError:
        print stamp
        return None


def create_alliances():
    api = eveapi.EVEAPIConnection()
    alliances = api.eve.AllianceList().alliances

    for alliance in alliances:

        if alliance.memberCount == 0:
            continue
        else:
            try:
                AllianceBulk.objects.create(
                    name=alliance.name,
                    shortname=alliance.shortName,
                    allianceid=alliance.allianceID,
                    executorcorpid=alliance.executorCorpID,
                    membercount=alliance.memberCount,
                    startdate=get_date_from_stamp(alliance.startDate),
                )
            except:
                print "This should not be happening"


def lookahead(iterable):
    it = iter(iterable)
    last = it.next()
    for val in it:
        yield last, False
        last = val
    yield last, True


START = 2563
END = 6000


def corporations_from_alliances():
    api = eveapi.EVEAPIConnection()
    alliances = api.eve.AllianceList().alliances

    piel = START
    temp = 0
    for alliance in alliances:
        if temp < piel:
            temp += 1
            continue

        print piel
        if alliance.memberCount == 0:
            piel += 1
            continue
        #now = datetime.now().replace(tzinfo=utc)

        counter = 0
        for member_corp, last in lookahead(alliance.memberCorporations):
            if CorporationBulk.objects.filter(
                corporationid=member_corp.corporationID
            ).exists():
                continue

            corp = api.corp.CorporationSheet(
                corporationID=member_corp.corporationID
            )

            try:
                corp = CorporationBulk(
                    #lastrefresh = now,
                    corporationid=corp.corporationID,
                    corporationname=corp.corporationName,
                    ticker=corp.ticker,
                    ceoid=corp.ceoID,
                    ceoname=corp.ceoName,
                    allianceid=corp.allianceID,
                    alliancename=corp.allianceName,
                    stationid=corp.stationID,
                    description=unicode(corp.description),
                    url=corp.url,
                    taxrate=int(corp.taxRate),
                    membercount=corp.memberCount,
                )
                corp.save()
                print corp.corporationname
            except Exception, e:
                print e

            if counter < 5:
                counter += 1
            else:
                counter = 0
                time.sleep(3)

            if last:
                piel += 1
                time.sleep(3)

        if piel == END:
            break


#create_alliances()
#corporations_from_alliances()

def check_corps():
    alliances = AllianceBulk.objects.all()
    counter = 0
    for alliance in alliances:
        try:
            CorporationBulk.objects.filter(allianceid=alliance.allianceid)
            counter += 1
        except CorporationBulk.DoesNotExist:
            print "Alliance: %s, ID: %d" % (
                alliance.name, alliance.allianceid
            )
    print counter

check_corps()
