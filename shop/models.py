from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)
    subcategories = models.ManyToManyField('self', blank=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField()
    description = models.TextField()
    price = models.PositiveSmallIntegerField(default=True)
    amount = models.PositiveSmallIntegerField(default=True)
    origin = models.CharField(max_length=100, null=True)
    weight = models.CharField(max_length=100, null=True)
    categories = models.ManyToManyField('shop1.Category', blank=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('number', 'title')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    product = models.ForeignKey(
        'shop1.Product',
        related_name='images',
        on_delete=models.CASCADE
        )


class Basket(models.Model):
    user = models.ForeignKey(get_user_model(),
    null=True,
    blank=True,
    on_delete=models.SET_NULL)
    status = models.TextField(default=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Пользователь {self.user} добавил в корзину '


class BasketItem(models.Model):
    basket = models.ForeignKey(
        'shop1.Basket',
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey('shop1.Product', on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1)


class Order(models.Model):
    WAITING = 'waiting'
    PROCESSING = 'processing'
    PROCESSED = 'processed'
    ORDER_STATUS = (
        (WAITING, WAITING.title()),
        (PROCESSING, PROCESSING.title()),
        (PROCESSED, PROCESSED.title())
    )

    basket = models.ForeignKey('shop1.Basket', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUS,
        default=WAITING
    )
    address = models.TextField()


