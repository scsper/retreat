from django.http import HttpResponse
from django.shortcuts import render

from retreat_app.models import Retreat

def index(request):
    return render(request, 'retreat_app/index.html')


def retreats(request):
    retreat_list = Retreat.objects.all()
    context = { 'retreat_list': retreat_list }

    # pass in the request, location of the template, and the variables the template uses
    return render(request, 'retreat_app/retreat_list.html', context)

def login(request):
    return render(request, 'retreat_app/login.html')