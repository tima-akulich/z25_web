from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True)
    price = models.FloatField()
    update_at_price = models.DateTimeField(auto_now=True)
    manufacturer = models.ForeignKey(
        'shop.Manufacturer',
        blank=True,
        on_delete=models.CASCADE
    )
    weight = models.FloatField()
    size = models.FloatField()
    related_products = models.ManyToManyField('shop.Product', blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.title}: {self.price}'


class Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Еденица измерения'
        verbose_name_plural = 'Еденицы измерения'

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    unit = models.ForeignKey('shop.Unit', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return f'{self.product}, {self.unit}: {self.quantity}'


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey('shop.Country', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


class Country(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.title


class Basket(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.user} {self.product}: {self.quantity}'


class Order(models.Model):
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery = models.ForeignKey('shop.Delivery', on_delete=models.CASCADE)
    pickup_point = models.ForeignKey(
        'shop.PickupPoint',
        on_delete=models.CASCADE
    )
    payment_type = models.ForeignKey(
        'shop.PaymentType',
        on_delete=models.CASCADE
    )
    order_status = models.ForeignKey(
        'shop.OrderStatus',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.user} {self.product}: {self.quantity}'


class Delivery(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'

    def __str__(self):
        return self.name


class PickupPoint(models.Model):
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Точка самовывоза'
        verbose_name_plural = 'Точки самовывоза'

    def __str__(self):
        return self.address


class PaymentType(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Тип оплаты'
        verbose_name_plural = 'Типы оплаты'

    def __str__(self):
        return self.title


class OrderStatus(models.Model):
    title = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

    def __str__(self):
        return self.title
