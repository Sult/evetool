from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
#from django.contrib import messages

from .models import Api
from .forms import ApiForm


def clear_character_session(request):
    del request.session['charpk']
    del request.session['access']
    del request.session['moderator']


@login_required
def apis(request):
    api_form = ApiForm(request.POST or None, user=request.user)

    if request.POST and api_form.is_valid():
        api_form.save(request.user)
        api_form = ApiForm(user=request.user)

    apis = Api.objects.filter(
        user=request.user,
        accounttype__in=[Api.CHARACTER, Api.ACCOUNT],
    )

    return render(
        request,
        "apis/apis.html",
        {
            "api_form": api_form,
            "apis": apis,
        }
    )


@login_required
def delete_api(request, pk):
    api = get_object_or_404(Api, pk=pk, user=request.user)
    api.delete_related()
    api.delete()

    if "charpk" in request.session:
        clear_character_session(request)

    return HttpResponseRedirect(reverse("apis"))


@login_required
def update_api(request, pk):
    api = get_object_or_404(Api, pk=pk, user=request.user)
    api.update()

    if "charpk" in request.session:
        clear_character_session(request)

    return HttpResponseRedirect(reverse("apis"))
