import time
from django.core.management.base import BaseCommand

from apps.apies.models import Api

from util import connection


# execute api tasks
class Command(BaseCommand):

    def handle(self, *args, **options):
        #update all characters with weekly cronjob
        for api in Api.objects.all():
            info = connection.apikeyinfo(api)
            for character in api.characterapi_set.all():
                #get cahracter from info by id, and update corporationid
                pass

            time.sleep(3)
