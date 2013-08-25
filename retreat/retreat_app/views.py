from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf # cross site request forgery

from retreat_app.models import Retreat

def index(request):
    return render(request, 'retreat_app/index.html')


@login_required
def retreats(request):
    retreat_list = Retreat.objects.all()
    context = { 'retreat_list': retreat_list }

    # pass in the request, location of the template, and the variables the template uses
    return render(request, 'retreat_app/retreat_list.html', context)


@login_required
def retreat_view(request, retreat_id):
    retreat = Retreat.objects.get(id=retreat_id)
    context = {'retreat': retreat}
    return render(request, 'retreat_app/retreat_view.html', context)


def login_view(request):
    context = {}
    context.update(csrf(request))
    return render(request, 'retreat_app/login.html', context)


def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/retreat/retreats/')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def invalid(request):
    return render(request, 'retreat_app/invalid.html')