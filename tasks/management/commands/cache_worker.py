import time
from optparse import make_option

from django.db import transaction
from django.core.management.base import BaseCommand

from tasks.models import EveApiCache


# execute api tasks
class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option(
            "--timer",
            action="store",
            type="float",
            dest="timer",
            default=0.3,
            help="""Change sleeptimer after no cache tasks are found. \
                Type is a float (default is 0.3 seconds)"""),
    )

    def handle(self, *args, **options):
        #get oldest task
        while True:
            with transaction.atomic():
                if EveApiCache.objects.filter(active=False).exists():
                    task = EveApiCache.objects.filter(active=False).first()
                    task.active = True
                    task.save()
                    self.task = task
                else:
                    self.task = False

            if self.task:
                self.task.set_cache()
                print self.task
                self.task.delete()
            else:
                time.sleep(options['timer'])
    handle.task = False
