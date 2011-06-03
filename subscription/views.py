# -*- coding: utf-8 -*-
# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from forms import SubscriptionForm
from subscription.models import Subscription
from subscription.utils import send_subscription_email

class SubscriptionCreateView(CreateView):
    form_class = SubscriptionForm
    model = Subscription

    def get_success_url(self):
        return reverse('subscription:success', args=[self.object.pk])

    def form_valid(self, form):
        response = super(SubscriptionCreateView, self).form_valid(form)
        # envia email
        send_subscription_email(self.object)

        return response

class SubscriptionSuccessView(DetailView):
    template_name = 'subscription/success.html'
    model = Subscription



'''
def new(request):
    form = SubscriptionForm(initial={
        'name': _(u'Entre com seu nome'),
        'cpf': _(u'Digite o seu CPF sem pontos'),
        'email': _(u'Informe o seu email'),
        'phone': _(u'99-99999999'),
    })
    context = RequestContext(request, {'form': form})
    return render_to_response('subscription/new.html', context)

def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form': form})
        return render_to_response('subscription/new.html', context)

    subscription = form.save()
    
    send_mail(
        subject=_(u'Inscrição no EventeX'),
        message=_(u'Obrigado por se inscrever no eventex!'),
        from_email=_('contato@eventex.com'),
        recipient_list=['macndesign@gmail.com'],
    )
    
    return HttpResponseRedirect(
        reverse('subscription:success', args=[subscription.pk])
    )

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)
'''