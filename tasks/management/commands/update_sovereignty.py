import sys
from django.core.management.base import BaseCommand

from apps.bulk.models import SovereigntyHolder, Sovereignty
import utils


# execute api tasks
class Command(BaseCommand):

    #handle is what actualy will be executed
    def handle(self, *args, **options):
        systems = utils.connection.api_request("Sovereignty").solarSystems
        for sov in systems:

            system, created = Sovereignty.objects.get_or_create(
                solarsystemid=sov.solarSystemID,
                solarsystemname=sov.solarSystemName,
            )
            try:
                holder = SovereigntyHolder.objects.filter(
                    sovereignty=system
                ).order_by("-last_refresh")[0]
                if holder.allianceid != int(sov.allianceID) or \
                    holder.factionid != int(sov.factionID) or \
                        holder.corporationid != int(sov.corporationID):
                    self.create_holder(sov, system)
            except IndexError:
                self.create_holder(sov, system)
            except:
                self.stdout.write(
                    sys.exc_info(),
                    "Unexpected error updating sovereignty:"
                )

    #crate new sovholder
    @staticmethod
    def create_holder(sov, system):
        try:
            SovereigntyHolder.objects.create(
                sovereignty=system,
                allianceid=int(sov.allianceID),
                corporationid=int(sov.corporationID),
                factionid=int(sov.factionID),
            )
        except:
            self.stdout.write(
                sys.exc_info(),
                "Unexpected error creating sovereignty:"
            )
