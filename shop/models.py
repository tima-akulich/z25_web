import base64

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    title = models.CharField(max_length=20, unique=True)
    subcategories = models.ManyToManyField('self', blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    categories = models.ManyToManyField('shop.Category', blank=True)
    price = models.FloatField()
    value = models.PositiveIntegerField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    image_base64 = models.TextField(default=None, null=True, blank=True)
    product = models.ForeignKey(
        'shop.Product',
        related_name='images',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if self.image:
            self.image_base64 = 'data:{content_type};base64,{data}'.format(
                content_type='jpeg',
                data=base64.b64encode(
                    self.image.file.read()
                ).decode()
            )
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        return self.image_base64 or self.image.url


class Basket(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BasketItem(models.Model):
    basket = models.ForeignKey(
        'shop.Basket',
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product}: {self.count}'


class Order(models.Model):
    WAITING = 'waiting'
    PROCESSING = 'processing'
    PROCESSED = 'processed'
    ORDER_STATUS = (
        (WAITING, WAITING.title()),
        (PROCESSING, PROCESSING.title()),
        (PROCESSED, PROCESSED.title())
    )

    basket = models.ForeignKey('shop.Basket', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUS,
        default=WAITING
    )
    address = models.TextField()


class RequestError(models.Model):
    exception_name = models.CharField(max_length=50)
    exception_value = models.CharField(max_length=250)
    exception_tb = models.TextField()
    request_method = models.CharField(max_length=10)
    path = models.CharField(max_length=500)
    query = JSONField()
    data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'{self.exception_name}: {self.exception_value}'

