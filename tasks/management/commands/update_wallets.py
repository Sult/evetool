import time
from django.core.management.base import BaseCommand

from apps.characters.models import CharacterApi


# execute api tasks
class Command(BaseCommand):

    def handle(self, *args, **options):
        #update all characters with weekly cronjob
        for character in CharacterApi.objects.all():
            if character.api.access_to("WalletJournal"):
                character.update_journal()
                time.sleep(3)
