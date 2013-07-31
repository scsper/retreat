from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from retreat_app.models import Retreat

def index(request):
    return render(request, 'retreat_app/index.html')


@login_required
def retreats(request):
    retreat_list = Retreat.objects.all()
    context = { 'retreat_list': retreat_list }

    # pass in the request, location of the template, and the variables the template uses
    return render(request, 'retreat_app/retreat_list.html', context)

def login_view(request):
    return render(request, 'retreat_app/login.html')

def validate_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/r/retreats/') # Redirect to a success page.

        #else:
            # Return a 'disabled account' error message
    #else:
        # Return an 'invalid login' error message

