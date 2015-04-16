# evetool
All in one eve website

Full api access player < corporation < alliance < coalition site.
Later will also implement extra features like marketprices killboard and more

For this project to work a couple steps have to be taken.
First of all change the secret key in config/settings.py

Setting up databases:
Download static dumps from (use latest postgres.dmp.bz2)
staticdump: https://www.fuzzwork.co.uk/dump/
<!-- images: https://developers.eveonline.com/resource/image-export-collection -->

create databases according to your settingsfile
and assign the corosponding owners
####create user named eve (this is needed for the eve online static dump)

load fixed database from dumpfile
pg_restore -d evetool_fixed /path/to/dump/file
more info: http://www.postgresql.org/docs/9.1/static/app-pgrestore.html


When migrating databases make sure to migrate the corrosponding database on modelchanges

Migrating databases:

./manage.py migrate

./manage.py migrate --database=evetool_bulk

./manage.py migrate --database=evetool_static


Next, set up cronjobs by using ./manage.py crontab | crontab -
Keep in mind this overwrites your crontab. add them manualy if this is not wanted (get the lines with ./manage.py crontab)

while running server, make sure to run at least 1 cache worker
./manage.py cache_worker





