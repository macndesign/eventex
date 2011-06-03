from django.conf.urls.defaults import patterns, url
from subscription.views import SubscriptionCreateView, SubscriptionSuccessView

urlpatterns = patterns('subscription.views',
    url(r'^$', SubscriptionCreateView.as_view(), name='subscribe'),
    url(r'^(?P<pk>\d+)/sucesso/$', SubscriptionSuccessView.as_view(), name='success'),
)

'''
urlpatterns = patterns('subscription.views',
    route(r'^$', GET='new', POST='create', name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)

'''