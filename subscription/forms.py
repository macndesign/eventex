# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import EMPTY_VALUES
from models import Subscription
from django.utils.translation import ugettext as _
import validators

class PhoneWidget(forms.MultiWidget):
    def __init__(self, ddd_maxlength=2, tel_maxlength=8, attrs=None):
        widgets = (
            forms.TextInput(attrs={'size': str(ddd_maxlength-1), 'maxlength': str(ddd_maxlength)}),
            forms.TextInput(attrs={'size': str(tel_maxlength-1), 'maxlength': str(tel_maxlength)})
        )
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if not value:
            return [None, None]
        return value.split('-')

class PhoneField(forms.MultiValueField):
    widget = PhoneWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.IntegerField()
        )
        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if not data_list:
            return None
        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'DDD inválido.'))
        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'Número inválido'))

        return '%s-%s' % tuple(data_list)

class SubscriptionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':'40'}))
    cpf = forms.CharField(
        widget=forms.TextInput(attrs={'size':'30', 'maxlength':'11'}),
        validators=[validators.CpfValidator],
        required=False
    )
    phone = PhoneField(required=False)

    class Meta:
        model = Subscription
        exclude = ('created_at', 'paid')

    # Email e CPF serão opicionais, mas precisa informar um dos dois
    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and \
            not self.cleaned_data.get('phone'):
            raise forms.ValidationError(
                _(u'Informe seu e-mail ou telefone.')
            )
        return self.cleaned_data
