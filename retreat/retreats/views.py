from django.shortcuts import render
from retreats.models import Retreat

def index(request):
    retreat_list = Retreat.objects.all()
    context = { 'retreat_list': retreat_list }
    return render(request, 'retreats/index.html', context)
