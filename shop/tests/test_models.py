from django.test import TestCase
from mock import patch, Mock
from django.utils.translation import activate

from shop.utils import get_random_number, multiplication

from shop.models import Category, CategoryTranslation


class TranslationTest(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(
            title='title',
            slug='slug'
        )
        CategoryTranslation.objects.create(
            lang='en',
            title='English title',
            item=self.category
        )
        CategoryTranslation.objects.create(
            lang='ru',
            title='Русское заглавие',
            item=self.category
        )

    def test_localization(self):
        res = self.category.localization
        self.assertEqual(res, 'English title')

        # get_language = Mock()

        # with patch('django.utils.translation.get_language', get_language):
            # print(mocked_object)
        activate('ru')
        res = self.category.localization
        # self.assertTrue(mocked_object.called)
        # self.assertEqual(mocked_object.call_count, 1)
        self.assertEqual(res, 'Русское заглавие')
        activate('be')
        res = self.category.localization
        self.assertEqual(res, self.category.id)

    def test_random_number(self):
        with patch('random.randint') as mocked:
            mocked.return_value = 5
            self.assertEqual(get_random_number(), 5)

            mocked.return_value = 543
            with self.assertRaises(Exception):
                get_random_number()

    @patch('shop.utils.get_random_number')
    def test_multiplication(self, mocked_multiplication):
        mocked_multiplication.side_effect = Exception('error')

        with self.assertRaises(Exception):
            multiplication(5)
