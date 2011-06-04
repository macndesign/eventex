# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.simple import direct_to_template
from core.models import Speaker, Talk

class HomepageView(TemplateView):
    template_name = 'index.html'

class TalkListView(TemplateView):
    template_name = 'core/talks.html'

    def get_context_data(self, **kwargs):
        context = super(TalkListView, self).get_context_data(**kwargs)

        context['morning_talks'] = Talk.objects.at_morning()
        context['afternoon_talks'] = Talk.objects.at_afternoon()

        return context

class TalkDetailView(DetailView):
    model = Talk
    context_object_name = 'talk'

class SpeakerDetailView(DetailView):
    model = Speaker
    context_object_name = 'speaker'


'''
def homepage(request):
    return direct_to_template(request, 'index.html')

def talks(request):
    return direct_to_template(request, 'core/talks.html', {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
    })

def talk_details(request, talk_id):
    talk = get_object_or_404(Talk, id=talk_id)
    return direct_to_template(request, 'core/talk_detail.html', {
        'talk': talk,
        'slides': talk.media_set.filter(type='SL'),
        'videos': talk.media_set.filter(type='YT'),
    })

def speaker(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return direct_to_template(request, 'core/speaker_detail.html',
                              {'speaker': speaker})
'''