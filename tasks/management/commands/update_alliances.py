import sys
from django.core.management.base import BaseCommand

from apps.bulk.models import Alliance
import utils


# execute api tasks
class Command(BaseCommand):

    #handle is what actualy will be executed
    def handle(self, *args, **options):
        #add new alliances
        alliances = utils.connection.api_request("AllianceList").alliances

        for alliance in alliances:

            if alliance.memberCount == 0:
                continue

            temp = self.update_alliance(alliance)
            if not temp:
                self.create_alliance(alliance)

    #update alliance
    def update_alliance(self, alliance):
        try:
            ally = Alliance.objects.get(
                name__iexact=str(alliance.name),
            )
            ally.name = str(alliance.name)
            ally.shortname = str(alliance.shortName)
            ally.allianceid = int(alliance.allianceID)
            ally.executorcorpid = int(alliance.executorCorpID)
            ally.membercount = int(alliance.memberCount)
            ally.save()

            if ally.membercount == 0:
                ally.delete()
            return True
        except Alliance.DoesNotExist:
            return False
        except:
            self.stdout.write(
                sys.exc_info(),
                "Unexpected error updating alliance:"
            )
            self.stdout.write("Problem on name: %s" % alliance.name)
            return False

    def create_alliance(self, alliance):
        try:
            Alliance.objects.create(
                name=str(alliance.name),
                shortname=str(alliance.shortName),
                allianceid=int(alliance.allianceID),
                executorcorpid=int(alliance.executorCorpID),
                membercount=int(alliance.memberCount),
                startdate=utils.common.convert_timestamp(alliance.startDate),
            )
        except:
            self.stdout.write(
                sys.exc_info(),
                "Unexpected error creating alliance:",
            )
            self.stdout.write("Problem on id: %s" % alliance.allianceID)
