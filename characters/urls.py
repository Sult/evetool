from django.conf.urls import patterns, url

from apps.characters import views

urlpatterns = patterns(
    '',
    url(
        r'^characters/$',
        views.characters,
        name='characters',
    ),
    url(
        r'^characters/(?P<pk>\d+)/$',
        views.select_character,
        name='select_character',
    ),
    #charactersheet
    url(
        r'^characters/sheet/$',
        views.character_sheet,
        name='character_sheet',
    ),
    url(
        r'^characters/sheet/data/$',
        views.character_sheet_data,
        name='character_sheet_data',
    ),

    #character skills
    url(
        r'^character/skills/$',
        views.character_skills,
        name='character_skills'
    ),
    url(
        r'^character/journal/$',
        views.character_journal,
        name='character_journal',
    ),
)
