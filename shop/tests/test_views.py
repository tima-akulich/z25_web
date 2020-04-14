from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from shop.models import Product


class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        get_user_model().objects.create_user(
            username='user',
            password='password'
        )

    def setUp(self):
        self.product = Product.objects.create(
            title='Title',
            price=10,
            value=20,
            published=True
        )

    def test_product_details_view(self):
        response = self.client.get(
            reverse('product_details', kwargs={'pk': self.product.pk}))
        # self.assertRedirects(response, settings.LOGIN_REDIRECT_URL, target_status_code=302)

        login_success = self.client.login(
            username='user',
            password='password'
        )
        self.assertTrue(login_success)
        response = self.client.get(reverse('product_details', kwargs={'pk': self.product.pk}))
        self.assertTemplateUsed(response, 'product_details.html')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('product_details', kwargs={'pk': 1000 }))
        self.assertEqual(response.status_code, 404)
