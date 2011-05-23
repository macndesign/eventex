from django.test import TestCase
from subscription.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):

    def test_if_form_has_no_paid_field(self):
        form = SubscriptionForm()
        self.assertFalse(form.fields.get('paid'))

    def test_returns_error_with_less_than_11_digits_in_cpf(self):
        form = SubscriptionForm({
            'name': 'User',
            'cpf': '123456789',
            'email': 'user@gmail.com',
            'phone': '85-99999999',
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors.get('cpf'))

    def test_returns_error_if_cpf_is_not_all_digits(self):
        form = SubscriptionForm({
            'name': 'User',
            'cpf': '123456789ab',
            'email': 'user@gmail.com',
            'phone': '85-87054624'
        })
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors.get('cpf'))
