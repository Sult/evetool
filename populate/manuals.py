from apps.bulk.models import Corporation, Character, Alliance
from apps.bulk.models import EmploymentHistory
from apps.bulk.models import Sovereignty, SovereigntyHolder
import utils
from utils.common import convert_timestamp
from utils.whoapi import who_connect, get_url, json_object


STARTER = 0


def create_characters():
    corps = Corporation.objects.all()
    counter = 0

    for corp in corps:
        counter += 1
        if counter < STARTER:
            continue
        print counter
        pages = True
        page = 0
        while pages:
            who_connect()
            url = get_url("corplist", corp.corporationid, page=page)
            data = json_object(url)
            for char in data['characters']:
                if not Character.objects.filter(
                    characterid=char['character_id']
                ).exists():
                    Character.objects.create(
                        characterid=char["character_id"],
                        corporationid=char["corporation_id"],
                        allianceid=char["alliance_id"],
                        charactername=char["name"],
                    )

            if len(data['characters']) == 200:
                page += 1
            else:
                pages = False


# def cahracter_corp_name():
#     for char in CharacterBulk.objects.all():
#         try:
#             corp = CorporationBulk.objects.get(
#                 corporationid=char.corporationid
#             )
#             char.corporationname = corp.corporationname
#             char.save()
#         except:
#             print "corpid %d does not exist" % char.corporationid


def add_sov_systems():
    systems = utils.connection.api_request("Sovereignty")
    for s in systems.solarSystems:
        # try:
        Sovereignty.objects.create(
            solarsystemid=s.solarSystemID,
            solarsystemname=s.solarSystemName,
        )
        # except:
        #     print "You fucked up mate"


def add_sov_holders():
    systems = utils.connection.api_request("Sovereignty")
    for s in systems.solarSystems:
        SovereigntyHolder.owner_change(s)


def create_alliances():
    alliances = utils.connection.api_request("AllianceList").alliances

    for alliance in alliances:

        if alliance.memberCount == 0:
            continue
        if Alliance.objects.filter(
            allianceid=alliance.allianceID,
        ).exists():
                continue
        else:
            try:
                Alliance.objects.create(
                    name=alliance.name,
                    shortname=alliance.shortName,
                    allianceid=alliance.allianceID,
                    executorcorpid=alliance.executorCorpID,
                    membercount=alliance.memberCount,
                    startdate=convert_timestamp(alliance.startDate),
                )
            except:
                print "This should not be happening"


START = 0


def corporations_from_alliances():

    piel = START
    temp = 0
    for alliance in utils.connection.api_request("AllianceList").alliances:
        if temp < piel:
            temp += 1
            continue

        print piel
        if alliance.memberCount == 0:
            piel += 1
            continue

        for member_corp in alliance.memberCorporations:
            if Corporation.objects.filter(
                corporationid=member_corp.corporationID
            ).exists():
                continue

            utils.connection.api_connect()
            corp = utils.connection.corporationsheet(
                corporationid=member_corp.corporationID
            )

            try:
                co = Corporation(
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
                co.save()
                print co.corporationname
            except Exception, e:
                print e

        piel += 1


def create_corps():
    alliances = []
    for alliance in Alliance.objects.all():
        if not Corporation.objects.filter(
            allianceid=alliance.allianceid
        ).exists():
            alliances.append(alliance.allianceid)

    corp_id_list = []
    for al in alliances:
        l = getattr(connection, "alliancecorporations")(al)
        corp_id_list.append(l)

    for corps in corp_id_list:
        for corp in corps:
            if Corporation.objects.filter(
                corporationid=corp.corporationid
            ).exists():
                continue

            c = getattr(connection, "corporationsheet")(
                corp.corporationid
            )

            try:
                co = Corporation(
                    corporationid=c.corporationID,
                    corporationname=c.corporationName,
                    ticker=c.ticker,
                    ceoid=c.ceoID,
                    ceoname=c.ceoName,
                    allianceid=c.allianceID,
                    alliancename=c.allianceName,
                    stationid=c.stationID,
                    description=unicode(c.description),
                    url=c.url,
                    taxrate=int(c.taxRate),
                    membercount=c.memberCount,
                )
                co.save()
                print co.corporationname
            except Exception, e:
                print e
