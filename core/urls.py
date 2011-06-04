from django.conf.urls.defaults import patterns, url
from core.views import HomepageView, TalkListView, TalkDetailView, SpeakerDetailView

urlpatterns = patterns('core.views',
    url(r'^$', HomepageView.as_view(), name='index'),
    url(r'^palestras/$', TalkListView.as_view(), name='talks'),
    url(r'^palestra/(?P<pk>\d+)/$', TalkDetailView.as_view(), name='talk_details'),
    url(r'^palestrante/(?P<slug>[-\w]+)/$', SpeakerDetailView.as_view(), name='speaker'),
)

'''
url(r'^$', 'homepage', name='index'),
url(r'^palestras/$', 'talks', name='talks'),
url(r'^palestra/(\d+)/$', 'talk_details', name='talk_details'),
url(r'^palestrante/([-\w]+)/$', 'speaker', name='speaker'),
'''
