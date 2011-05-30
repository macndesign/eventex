# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from core.models import Speaker, Talk

def homepage(request):
    return direct_to_template(request, 'index.html')

def speaker(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return direct_to_template(request, 'core/speaker.html',
                              {'speaker': speaker})

def talks(request):
    return direct_to_template(request, 'core/talks.html', {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    })

def talk_details(request, talk_id):
    talk = get_object_or_404(Talk, id=talk_id)
    return direct_to_template(request, 'core/talk.html', {
        'talk': talk,
        'slides': talk.media_set.filter(type='SL'),
        'videos': talk.media_set.filter(type='YT'),
    })
