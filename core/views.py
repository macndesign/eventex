from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def homepage(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)
