from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from apps.characters.models import CharacterApi


#make sure the session is filled with a valid character for the user,
#otherwise redirect back to the characters page
def valid_character_selected(view_func):
    def check_session(request, *args, **kwargs):
        if "charpk" in request.session:
            if not request.session['moderator']:
                if not CharacterApi.objects.get(
                    characterid=request.session['charpk'],
                    api__user=request.user
                ).exists():
                    return HttpResponseRedirect(reverse("characters"))
        else:
            return HttpResponseRedirect(reverse("characters"))
        return view_func(request, *args, **kwargs)
    return check_session
