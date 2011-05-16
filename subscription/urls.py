from django.conf.urls.defaults import patterns, url
from route import route

urlpatterns = patterns('subscription.views',
    route(r'^$', GET='new', POST='create', name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)