from django.core.urlresolvers import reverse
from django.test import TestCase
from subscription.forms import SubscriptionForm

class SubscriptionUrlTest(TestCase):
    
    def test_successful_get_subscription_page(self):
        response = self.client.get(reverse('subscription:subscribe'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'subscription/new.html')
        self.assertTrue(isinstance(response.context['form'], SubscriptionForm))

    def test_redirects_to_success_after_valid_post(self):
        response = self.client.post(reverse('subscription:subscribe'), {
            'name': 'Mario Chaves',
            'cpf': '11111111111',
            'email': 'macndesign@gmail.com',
            'phone': '85-34942660'
        })
        self.assertRedirects(response, reverse('subscription:success', args=[1]))
