from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
#from django.contrib import messages

from apps.apies.models import Api
from apps.apies.forms import ApiForm


def clear_character_session(request):
    del request.session['charpk']
    del request.session['access']
    del request.session['moderator']


@login_required
def apies(request):
    api_form = ApiForm(request.POST or None, user=request.user)

    if request.POST and api_form.is_valid():
        api_form.save(request.user)
        api_form = ApiForm(user=request.user)

    char_apies = Api.objects.filter(
        user=request.user,
        accounttype__in=[Api.CHARACTER, Api.ACCOUNT],
    )
    corp_apies = Api.objects.filter(
        user=request.user,
        accounttype=Api.CORPORATION,
    )
    return render(
        request,
        "apies/apies.html",
        {
            "api_form": api_form,
            "char_apies": char_apies,
            "corp_apies": corp_apies
        }
    )


@login_required
def delete_api(request, pk):
    api = get_object_or_404(Api, pk=pk, user=request.user)
    api.delete_related()
    api.delete()

    if "charpk" in request.session:
        clear_character_session(request)

    return HttpResponseRedirect(reverse("apies"))


@login_required
def update_api(request, pk):
    api = get_object_or_404(Api, pk=pk, user=request.user)
    api.update()

    if "charpk" in request.session:
        clear_character_session(request)

    return HttpResponseRedirect(reverse("apies"))
