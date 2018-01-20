from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from utility import *
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def main_base_view(request):
    dictionary = dict(request=request)
    dictionary.update(csrf(request))
    return render_to_response('main/main_base.html', dictionary)


def login(request):
    if request.method == 'POST':
        username = request.POST['u']
        password = request.POST['p']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request=request, user=user)
            return HttpResponseRedirect(reverse('principal:main_base'))
        else:
            msg_to_html = custom_message('Invalid Credentials', TagType.danger)
            dictionary = dict(request=request, messages=msg_to_html)
            dictionary.update(csrf(request))
        return render_to_response('main/main_base.html', dictionary)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # is valid returns true
            form.save()
            msg_to_html = custom_message('User Created', TagType.success)
            dictionary = dict(request=request, messages=msg_to_html)
            dictionary.update(csrf(request))
            return render_to_response('main/main_base.html', dictionary)
    else:
        form = UserCreationForm()
        dictionary = dict(request=request, form=form)
        dictionary.update(csrf(request))
        return render(request, 'account/signup.html', dictionary)
