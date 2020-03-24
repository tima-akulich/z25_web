from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField()
    description = models.TextField()
    price = models.PositiveSmallIntegerField(default=True)
    amount = models.PositiveSmallIntegerField(default=True)
    origin = models.CharField(max_length=100, default=None)
    weight = models.CharField(max_length=100, default=None)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('number', 'title')

    def __str__(self):
        return self.title


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    elements = models.ManyToManyField('shop.BasketElements', blank=True)
    status = models.TextField(default=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Пользователь {self.user} добавил в корзину {self.product}. Количество: {self.number}'


class BasketElements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100, default=None)
    element = models.ForeignKey('shop.Product', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'

    def __str__(self):
        return f'{self.user} - {self.element}'

