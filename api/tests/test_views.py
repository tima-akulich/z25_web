from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from shop.models import Product, Category


class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        get_user_model().objects.create_user(
            username='user',
            password='password'
        )

    def setUp(self):
        self.category_list = []
        self.product_list = []
        for number_category in range(1, 3):
            self.category_list.append(Category.objects.create(
                title=f'Category {number_category}',
                slug=f'category-{number_category}'
            ))
        for number_product in range(1, 4):
            self.product_list.append(Product.objects.create(
                title=f'Product {number_product}',
                price=10 * number_product,
                value=20 * number_product,
                published=True
            ))
        for i, product in enumerate(self.product_list):
            if i < 2:
                product.categories.add(self.category_list[i])
            else:
                product.categories.add(*self.category_list)

    def test_product_list_view(self):
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, 401)
        login_success = self.client.login(
            username='user',
            password='password'
        )
        self.assertTrue(login_success)
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, 200)
        # response = self.client.get(reverse(
        #     'products_list',
        #     kwargs={'pk': self.category_list[0].id}
        # ))
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(
            [item['id'] for item in response.json()['results']],
            [item.id for item in self.product_list]
        )
        self.client.logout()

    def test_basket_item_view(self):
        response = self.client.get(reverse('basket-api'))
        self.assertEqual(response.status_code, 401)
        self.client.login(
            username='user',
            password='password'
        )
        # response = self.client.get(reverse('basket-api'))
        # self.assertEqual(response.status_code, 404)
