from django.http import HttpResponse
from django.template import RequestContext, loader

from retreats.models import Retreat

def index(request):
    retreat_list = Retreat.objects.all()
    template = loader.get_template('retreats/index.html')
    context = RequestContext(request, {
        'retreat_list': retreat_list,
    })
    return HttpResponse(template.render(context))
