from datetime import datetime
import base64

from django.contrib.postgres.fields import JSONField

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class Category(models.Model):
    title = models.CharField(_('Title'),max_length=20, unique=True)
    subcategories = models.ManyToManyField('self', blank=True,verbose_name=_('Subcategories'))
    slug = models.SlugField(_('Slug'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    number = models.PositiveSmallIntegerField(_('Number'))
    description = models.TextField(_('Description'))
    price = models.PositiveSmallIntegerField(_('Price'),default=True,)
    amount = models.PositiveSmallIntegerField(_('Amount'), default=True)
    origin = models.CharField(_('Origin'), max_length=100, null=True)
    weight = models.CharField(_('Weight'), max_length=100, null=True)
    categories = models.ManyToManyField('shop.Category', blank=True, verbose_name=_('Categories'))
    published = models.BooleanField(_('Published'), default=False)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ('number', 'title')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    description = models.TextField(_('Description'))
    image = models.ImageField(_('Image'), upload_to='products/%Y/%m/%d/')
    image_base64 = models.TextField(_('Image_base64'), default=None, null=True, blank=True)
    product = models.ForeignKey(
        'shop.Product',
        related_name='images',
        on_delete=models.CASCADE,
        )

    class Meta:
        verbose_name = _('Product_image')
        verbose_name_plural = _('Products_images')



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
        on_delete=models.SET_NULL,
        verbose_name=_('User')
    )
    created_at = models.DateTimeField(_('Created_at'),auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated_at'),auto_now=True)


class BasketItem(models.Model):
    basket = models.ForeignKey(
        'shop.Basket',
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name=_('Basket')
    )
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, verbose_name=_('Product'))
    count = models.PositiveSmallIntegerField(_('Count'), default=1)

    def __str__(self):
        return f'{self.product}'


class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('User')

    )
    basket = models.ForeignKey('shop.Basket', on_delete=models.CASCADE, verbose_name=_('Basket'))
    first_name = models.CharField(_('First_name'),max_length=50)
    last_name = models.CharField(_('Last_name'),max_length=50)
    email = models.CharField(_('Email'),max_length=50)
    address = models.CharField(_('Address'),max_length=50)
    created_at = models.DateTimeField(_('Created_at'),auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated_at'),auto_now=True)
    paid = models.BooleanField(_('Paid'), default=False)
    WAITING = _('waiting')
    PROCESSING = _('processing')
    PROCESSED = _('processed')
    ORDER_STATUS = (
        (WAITING, WAITING.title()),
        (PROCESSING, PROCESSING.title()),
        (PROCESSED, PROCESSED.title())
    )

    statuses = models.CharField(
        max_length=10,
        choices=ORDER_STATUS,
        default=WAITING,
        verbose_name=_('Statuses')

    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return 'Order {}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE,verbose_name=_('Order'))
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name=_('Product'))
    price = models.PositiveIntegerField(_('Price'),default=1)
    quantity = models.PositiveIntegerField(_('quantity'), default=1)

    def __str__(self):
        return '{}'.format(self.id)


class RequestError(models.Model):
    exception_name = models.CharField(_('Exception_name'), max_length=50)
    exception_value = models.CharField(_('Exception_value'), max_length=250)
    exception_tb = models.TextField(_('Exception_tb'))
    request_method = models.CharField(_('Request_method'), max_length=10)
    path = models.CharField(_('Path'), max_length=500)
    query = JSONField()
    data = JSONField()
    created_at = models.DateTimeField(_('Created_at'), auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )
        verbose_name = _('Request error')
        verbose_name_plural = _('Request errors')

    def __str__(self):
        return f'{self.exception_name}: {self.exception_value}'

