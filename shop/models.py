from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE)
    price = models.MoneyField(max_digits=10, decimal_places=2)
    manufacturer = models.ForeignKey('shop.Manufacturer', on_delete=models.CASCADE)
    info = models.TextField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('title', 'price')

    def __str__(self):
        return f'{self.title} {self.price}'


class Manufacturer(models.Model):
    title = models.CharField(max_length=100, unique=True)
    info = models.TextField()

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = ('title', )

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    info = models.TextField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title', )

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    products = models.ManyToManyField('shop.Product', blank=True)
    data = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    total = models.MoneyField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user} - {self.products} - {self.data} - {self.total}'
