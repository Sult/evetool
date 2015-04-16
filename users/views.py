from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib import messages

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.users.models import UserControl
from apps.users.forms import LoginForm, RegistrationForm, ContactMailForm
from apps.blog.models import Article


def index(request):
    login_form = LoginForm(request.POST or None)

    if request.POST and login_form.is_valid():
        user = login_form.login(request)
        if user:
            if not user.usercontrol.confirmed:
                return HttpResponseRedirect(reverse("not_accepted"))
            login(request, user)
            return HttpResponseRedirect(request.POST.get('next') or reverse('index'))

    #get articles
    if request.user.is_authenticated():
        articles = Article.objects.filter(published=True, public=False, corp=True).order_by("-sticky", "-created")
    else:
        articles = Article.objects.filter(published=True, public=True, corp=True).order_by("-sticky", "-created")

    #paginator = Paginator(articles, 10, request=request)
    #page = request.GET.get('page', 1)
    #try:
        #articles = paginator.page(page)
    #except PageNotAnInteger:
        #articles = paginator.page(1)
    #except EmptyPage:
        #articles = paginator.page(paginator.num_pages)

    return render(request, "users/index.html", {"login_form": login_form, "articles": articles, 'next': request.GET.get('next', '')})







def not_accepted(request):
    return render(request, "users/not_accepted.html")



# Register new user
def register_user(request):
    #make sure user is not already logged in
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("index"))

    form = RegistrationForm(request.POST or None)
    login_form = LoginForm()
    # False till someone fills in and sends
    if request.POST and form.is_valid():
        new_user = form.save()
        UserControl.objects.create(user=new_user)
        #send confiermationmail blabla

        return HttpResponseRedirect(reverse('register succes'))

    return render(request, 'users/register.html', {'form': form, "login_form": login_form})



def register_succes(request):
    login_form = LoginForm(request.POST or None)
    return render(request, "users/register_succes.html", {"login_form": login_form})



@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))



########### Information pages
def contact(request):
    login_form = LoginForm()
    contact_form = ContactMailForm(request.POST or None)
    if request.POST and contact_form.is_valid():
        contact_form.save()
        messages.add_message(request, messages.SUCCESS, 'You will receive a reply shortly.')


    return render(request, "users/contact.html", {"login_form": login_form, "contact_form": contact_form})
