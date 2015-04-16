import os
from django.core.management.base import BaseCommand
from django.conf import settings


# setup cronjobs
# You can add these by adding ./manage.py crontab to contrab -e
# or overwrite crontab with ./manage.py crontab | crontab -
# crontab command asumes your virtualenv has the same name as your project
# end is located in the same directory as your project folder
# crontab spreads tasks at different times
class Command(BaseCommand):
    def handle(self, *args, **options):
        venv_path = os.path.join(
            settings.BASE_DIR, "../", "venv",
            settings.PROJECT_NAME, "bin", "python"
        )
        task_path = task = os.path.join(
            settings.BASE_DIR, "manage.py"
        )

        self.stdout.write("# http://www.unix.com/man-page/linux/5/crontab/")

        #add regular wallet updates
        cron = "@weekly"
        task = "update_wallets"
        self.stdout.write("%s %s %s %s" % (cron, venv_path, task_path, task))

        # update alliances
        #daily at 01:00
        cron = "0 1 * * *"
        task = "update_alliances"
        self.stdout.write("%s %s %s %s" % (cron, venv_path, task_path, task))

        #update sovereingthy
        #every 2 hours ad 15 minutes after hour
        cron = "15 */2 * * *"
        task = "update_sovereignty"
        self.stdout.write("%s %s %s %s" % (cron, venv_path, task_path, task))

        #update character corporation
        #check this every 2 hours
        cron = "30 */2 * * *"
        task = "update_character_corp"
        self.stdout.write("%s %s %s %s" % (cron, venv_path, task_path, task))
