# -*- coding: utf-8 -*-
# Create your views here.
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from forms import SubscriptionForm
from subscription.models import Subscription
from django.utils.translation import ugettext as _

def new(request):
    form = SubscriptionForm(initial={
        'name': _(u'Entre com seu nome'),
        'cpf': _(u'Digite o seu CPF sem pontos'),
        'email': _(u'Informe o seu email'),
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
