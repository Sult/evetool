import urllib2
import os
import time

from django.db.models import get_model
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.cache import cache

import eveapi


#get data from cache
def get_cache(key):
    return cache.get(key)


#set data to cache
def set_cache(key, data, timeout):
    cache.set(key, data, timeout)


# generate cachkey for
def generate_cache_key(category, key, api=None, **kwargs):
    cache_key = "%s_%s" % (category, key)

    if api:
        cache_key += "_%d" % api.pk

    for key, value in kwargs.iteritems():
        cache_key += "_%s_%s" % (key, value)

    return cache_key


#create connection to eveapi. only allows x-requests per second
def api_connect():
    timestamp = int(time.time())
    if api_connect.timestamp == timestamp:
        api_connect.counter += 1
        if api_connect.counter == settings.EVE_API_REQUESTS:
        #if api_connect.counter == 10:
            time.sleep(1)
            api_connect.counter = 0
            api_connect.timestamp = timestamp
    else:
        api_connect.timestamp = timestamp
        api_connect.counter = 0
    return eveapi.EVEAPIConnection()
api_connect.timestamp = int(time.time())
api_connect.counter = 0


#create an authenticated connection with the eveapi (personal data)
def auth_connect(api):
    result = api_connect().auth(keyID=api.key, vCode=api.vcode)
    return result


#### Needed outside of cache #####
def apikeyinfo(api):
    auth = auth_connect(api)
    return auth.account.APIKeyInfo()


def accountstatus(api):
    auth = auth_connect(api)
    return auth.account.AccountStatus()


def corporationsheet(corporationid):
    api = api_connect()
    return api.corp.CorporationSheet(corporationId=corporationid)


###### CREATE ICONS/IMAGES #############

#get icon from eve image database
def icon_url(path, pk, size):
    """ Explination: https://image.eveonline.com/ """

    if path == "Character":
        filetype = "jpg"
    else:
        filetype = "png"
    return "http://image.eveonline.com/%s/%d_%d.%s" % \
        (path, pk, size, filetype)


# get icon model from object
def icon_model(obj):
    model_name = obj._meta.object_name
    model = get_model(obj._meta.app_label, model_name + "Icon")
    return model


#create or overwrite old icon
def update_icons(obj, pk, icon_type):
    model = icon_model(obj)
    sizes = model.icon_sizes()

    for s in sizes:
        url = icon_url(icon_type, pk, s)
        #create_or_overwrite_icon(model, obj, pk, s)

        temp, created = model.objects.get_or_create(
            relation=obj,
            typeid=pk,
            size=s,
        )
        #result = urllib.urlretrieve(url)
        #temp.icon.save(os.path.basename(url), File(open(result[0])))
        #temp.save()
        img = NamedTemporaryFile(delete=True)
        img.write(urllib2.urlopen(url).read())
        img.flush()
        temp.icon.save(os.path.basename(url), File(img))
        temp.save()








# #get
#data from api. obj should only be CharacterApi and CorporationApi objects.
# def api_request(key, api=None, obj=None, **kwargs):
#     cache_key = generate_cache_key(key, api, obj, **kwargs)
#     result = get_cache(cache_key)
#     if not result:
#         temp = api_request.dict[key]
#         result = temp['method'](api=api, obj=obj, **kwargs)
#         set_cache(cache_key, result, temp['timer'])
#     return result


# #create connection to eveapi. only allows x-requests per second
# def api_connect():
#     timestamp = int(time.time())
#     if api_connect.timestamp == timestamp:
#         api_connect.counter += 1
#         if api_connect.counter == settings.EVE_API_REQUESTS:
#         #if api_connect.counter == 10:
#             time.sleep(1)
#             api_connect.counter = 0
#             api_connect.timestamp = timestamp
#             print timestamp
#     else:
#         api_connect.timestamp = timestamp
#         api_connect.counter = 0
#     return eveapi.EVEAPIConnection()
# api_connect.timestamp = int(time.time())
# api_connect.counter = 0


# #create an authenticated connection with the eveapi (personal data)
# def auth_connect(api):
#     result = api_connect().auth(keyID=api.key, vCode=api.vcode)
#     return result


# ##### Allapi data request functions to load in the APIDICT






# def accountbalance(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.AccountBalance(
#             characterID=obj.characterid
#         )
#     else:
#         return auth.corp.AccountBalance(
#             corporationID=obj.corporationid
#         )


# def assetlist(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.AssetList(characterID=obj.characterid)
#     else:
#         return auth.corp.AssetList(
#             corporationID=obj.corporationid
#         )


# def callendareventattendees(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.CallendarEventAttendees(
#         characterID=obj.characterid,
#         eventIDs=kwargs['eventids']
#     )


# def characterinfo(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.CharacterInfo(characterID=kwargs['characterid'])


# def characterinfoauth(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.eve.CharacterInfo(characterID=obj.characterid)


# def charactersheet(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.CharacterSheet(characterID=obj.characterid)


# def contactlist(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.ContactList(characterID=obj.characterid)
#     else:
#         return auth.corp.ContactList(corporationID=obj.corporationid)


# def contactnotifications(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.ContactNotifications(
#         characterID=obj.characterid
#     )


# def containerlog(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.ContainerLog(characterID=obj.characterid)


# def contracts(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.Contracts(characterID=obj.characterid)
#     else:
#         return auth.corp.Contracts()


#


# def corporationsheetauth(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.CorporationSheet()


# def facwarstats(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.FacWarStats(characterID=obj.characterid)
#     else:
#         return auth.corp.FacWarStats()


# def industryjobs(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.IndustryJobs(characterID=obj.characterid)
#     else:
#         return auth.corp.IndustryJobs()


# def killlog(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.KillMails(characterID=obj.characterid)
#     else:
#         return auth.corp.KillMails()


# def locations(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.Locations(
#             characterID=obj.characterid,
#             IDs=kwargs['ids']
#         )
#     else:
#         return auth.corp.Locations(IDs=kwargs['ids'])


# def mailbodies(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.MailBodies(
#         characterID=obj.characterid,
#         ids=kwargs["ids"]
#     )


# def mailmessages(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.MailMessages(characterID=obj.characterid)


# def mailinglists(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.MailingLists(characterID=obj.characterid)


# def marketorders(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.MarketOrders(characterID=obj.characterid)
#     else:
#         return auth.corp.MarketOrders()


# def medals(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.Medals(characterID=obj.characterid)
#     else:
#         return auth.corp.Medals()


# def membermedals(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.MemberMedals()


# def membersecurity(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.MemberSecurity()


# def membersecuritylog(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.MemberSecurityLog()


# def membertrackingextended(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.MemberTracking(extended=1)


# def membertrackinglimited(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.MemberTracking()


# def notificationtexts(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.NotificationTexts(characterID=obj.characterid)


# def notifications(api=None, obj=None, *kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.Notifications(charcterID=obj.characterid)


# def outpostlist(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.OutpostList(characterID=obj.characterid)


# def outpostservicedetail(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.OutpostServiceDetail(
#         characterID=obj.characterid,
#         itemID=kwargs['itemid'],
#     )


# def research(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.Research(characterID=obj.characterid)


# def shareholders(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.Shareholders(characterID=obj.characterid)


# def skillintraining(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.SkillInTraining(characterID=obj.characterid)


# def skillqueue(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.SkillQueue(characterID=obj.characterid)


# def standings(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.Standings(characterID=obj.characterid)
#     else:
#         return auth.corp.Standings(characterID=obj.characterid)


# def starbasedetail(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.StarbaseDetail(itemID=kwargs['itemid'])


# def starbaselist(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.StarbaseList()


# def titles(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.corp.Titles(characterID=obj.characterid)


# def upcomingcalendarevents(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     return auth.char.UpcomingCalendarEvents(
#         characterID=obj.characterid
#     )


# def walletjournal(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)

#     rowcount = 50
#     if "rowcount" in kwargs:
#         rowcount = kwargs['rowcount']

#     if obj.__class__ == CharacterApi:
#         if "fromid" in kwargs:
#             return auth.char.WalletJournal(
#                 characterID=obj.characterid,
#                 rowCount=rowcount,
#                 fromID=kwargs['fromid'],
#             )

#         return auth.char.WalletJournal(
#             characterID=obj.characterid,
#             rowCount=rowcount,
#         )
#     else:
#         #TODO: needs testing
#         if "fromid" in kwargs:
#             return auth.char.WalletJournal(
#                 accountKey=kwargs['accountkey'],
#                 rowCount=rowcount,
#                 fromID=kwargs['fromid'],
#             )
#         return auth.char.WalletJournal(
#             accountKey=kwargs['accountkey'],
#             rowCount=kwargs['rowcount'],
#         )


# def wallettransactions(api=None, obj=None, **kwargs):
#     auth = auth_connect(obj.api)
#     if obj.__class__ == CharacterApi:
#         return auth.char.WalletTransactions(
#             characterID=obj.characterid,
#             rowCount=kwargs['rowcount'],
#         )
#     else:
#         return auth.char.WalletTransactions(
#             accountKey=kwargs['accountkey'],
#             rowCount=kwargs['rowcount'],
#         )


# def alliancelist(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.AllianceList()


# def characteraffiliation(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.CharacterAffiliation(ids=kwargs['ids'])


# def characterid(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.CharacterID(names=kwargs['names'])


# def charactername(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.CharacterName(ids=kwargs['ids'])


# def conquerablestationlist(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.ConquerableStationList()


# def errolist(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.ErrorList()


# def facwarstatspublic(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.FacWarStats()


# def facwartopstats(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.FacWarTopStats()


# def reftypes(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.RefTypes()


# def typename(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.TypeName(ids=kwargs['ids'])


# def skilltree(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.eve.SkillTree()


# def facwarsystems(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.map.FacWarSystems()


# def jumps(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.map.Jumps()


# def kills(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.map.Kills()


# def sovereignty(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.map.Sovereignty()


# def serverstatus(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.server.ServerStatus()


# def calllist(api=None, obj=None, **kwargs):
#     api = api_connect()
#     return api.API.CallList()


# # returns all corporations of an alliance by allianceid
# def alliancecorporations(allianceid):
#     """ returns a list of namedtuples that hold corporationid
#      and startdate(timestamp) """

#     api = api_connect()
#     alliances = api.eve.AllianceList().alliances
#     row = alliances.Get(allianceid, False)
#     result = []
#     if row and row.memberCount > 0:
#         MemberCorporation = namedtuple(
#             "MemberCorporation",
#             "corporationid startdate"
#         )
#         for corp in row.memberCorporations:
#             result.append(MemberCorporation(
#                 corporationid=corp.corporationID,
#                 startdate=corp.startDate)
#             )
#     return result





# #Seting up apidict for api_data function
# APIDICT = {
#     #account lookups
#     'AccountStatus': {
#         "method": accountstatus,
#         "timer": 60 * 5,
#     },
#     'ApiKeyInfo': {
#         "method": apikeyinfo,
#         "timer": 60 * 1,
#     },

#     #authenticated requests
#     'AccountBalance': {
#         "method": accountbalance,
#         "timer": 60 * 5,
#     },
#     'AssetList': {
#         "method": assetlist,
#         "timer": 60 * 10,
#     },
#     'CalendarEventAttendees':
#     {
#         "method": callendareventattendees,
#         "timer": 60 * 60,
#     },
#     'CharacterInfo': {
#         "method": characterinfo,
#         "timer": 60 * 5,
#     },
#     'CharacterInfoAuth': {
#         "method": characterinfoauth,
#         "timer": 60 * 5,
#     },
#     'CharacterSheet': {
#         "method": charactersheet,
#         "timer": 60 * 5,
#     },
#     'ContactList': {
#         "method": contactlist,
#         "timer": 60 * 5,
#     },
#     'ContactNotifications': {
#         "method": contactnotifications,
#         "timer": 60 * 5,
#     },
#     'ContainerLog': {
#         "method": containerlog,
#         "timer": 60 * 10,
#     },
#     'Contracts': {
#         "method": contracts,
#         "timer": 60 * 5,
#     },
#     'CorporationSheet': {
#         "method": corporationsheet,
#         "timer": 60 * 5,
#     },
#     'CorporationSheetAuth': {
#         "method": corporationsheetauth,
#         "timer": 60 * 5,
#     },
#     'FacWarStats': {
#         "method": facwarstats,
#         "timer": 60 * 10,
#     },
#     'IndustryJobs': {
#         "method": industryjobs,
#         "timer": 60 * 5,
#     },
#     'KillLog': {
#         "method": killlog,
#         "timer": 60 * 5,
#     },
#     'Locations': {
#         "method": locations,
#         "timer": 60 * 5,
#     },
#     'MailBodies': {
#         "method": mailbodies,
#         "timer": 60 * 10,
#     },
#     'MailMessages': {
#         "method": mailmessages,
#         "timer": 60 * 10,
#     },
#     'MailingLists': {
#         "method": mailinglists,
#         "timer": 60 * 30,
#     },
#     'MarketOrders': {
#         "method": marketorders,
#         "timer": 60 * 5,
#     },
#     'Medals': {
#         "method": medals,
#         "timer": 60 * 15,
#     },
#     'MemberMedals': {
#         "method": membermedals,
#         "timer": 60 * 15,
#     },
#     'MemberSecurity': {
#         "method": membersecurity,
#         "timer": 60 * 10,
#     },
#     'MemberSecurityLog': {
#         "method": membersecuritylog,
#         "timer": 60 * 10,
#     },
#     'MemberTrackingExtended': {
#         "method": membertrackingextended,
#         "timer": 60 * 15,
#     },
#     'MemberTrackingLimited': {
#         "method": membertrackinglimited,
#         "timer": 60 * 15,
#     },
#     'NotificationTexts': {
#         "method": notificationtexts,
#         "timer": 60 * 15,
#     },
#     'Notifications': {
#         "method": notifications,
#         "timer": 60 * 15,
#     },
#     'OutpostList': {
#         "method": outpostlist,
#         "timer": 60 * 5,
#     },
#     'OutpostServiceDetail': {
#         "method": outpostservicedetail,
#         "timer": 60 * 5,
#     },
#     'Research': {
#         "method": research,
#         "timer": 60 * 5,
#     },
#     'Shareholders': {
#         "method": shareholders,
#         "timer": 60 * 5,
#     },
#     'SkillInTraining': {
#         "method": skillintraining,
#         "timer": 60 * 5,
#     },
#     'SkillQueue': {
#         "method": skillqueue,
#         "timer": 60 * 5,
#     },
#     'Standings': {
#         "method": standings,
#         "timer": 60 * 10,
#     },
#     'StarbaseDetail': {
#         "method": starbasedetail,
#         "timer": 60 * 5,
#     },
#     'StarbaseList': {
#         "method": starbaselist,
#         "timer": 60 * 15,
#     },
#     'Titles': {
#         "method": titles,
#         "timer": 60 * 5,
#     },
#     'UpcomingCalendarEvents': {
#         "method": upcomingcalendarevents,
#         "timer": 60 * 5,
#     },
#     'WalletJournal': {
#         "method": walletjournal,
#         "timer": 60 * 3,
#     },
#     'WalletTransactions': {
#         "method": wallettransactions,
#         "timer": 60 * 3,
#     },

#     #eve public access
#     'AllianceList': {
#         "method": alliancelist,
#         "timer": 60 * 60,
#     },
#     'CharacterAffiliation': {
#         "method": characteraffiliation,
#         "timer": 60 * 5,
#     },
#     'CharacterID': {
#         "method": characterid,
#         "timer": 60 * 60,
#     },
#     'CharacterName': {
#         "method": charactername,
#         "timer": 60 * 60,
#     },
#     'ConquerableStationList': {
#         "method": conquerablestationlist,
#         "timer": 60 * 60,
#     },
#     'ErrorList': {
#         "method": errolist,
#         "timer": 60 * 60,
#     },
#     'FacWarStatsPublic': {
#         "method": facwarstatspublic,
#         "timer": 60 * 5,
#     },
#     'FacWarTopStats': {
#         "method": facwartopstats,
#         "timer": 60 * 5,
#     },
#     'RefTypes': {
#         "method": reftypes,
#         "timer": 60 * 60,
#     },
#     'SkillTree': {
#         "method": skilltree,
#         "timer": 60 * 60,
#     },
#     'TypeName': {
#         "method": 60 * 60,
#         "timer": typename,
#     },
#     'FacWarSystems': {
#         "method": facwarsystems,
#         "timer": 60 * 5,
#     },
#     'Jumps': {
#         "method": jumps,
#         "timer": 60 * 5,
#     },
#     'Kills': {
#         "method": kills,
#         "timer": 60 * 5,
#     },
#     'Sovereignty': {
#         "method": sovereignty,
#         "timer": 60 * 10,
#     },
#     'ServerStatus': {
#         "method": serverstatus,
#         "timer": 60 * 1,
#     },
#     'CallList': {
#         "method": calllist,
#         "timer": 60 * 60,
#     },
# }
# api_request.dict = APIDICT
