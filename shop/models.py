import base64

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_('Title'), max_length=20, unique=True)
    subcategories = models.ManyToManyField(
        'self',
        blank=True,
        verbose_name=_('Subcategories')
    )
    slug = models.SlugField(_('Slug'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    categories = models.ManyToManyField(
        'shop.Category',
        blank=True,
        verbose_name=_('Categories')
    )
    price = models.FloatField(_('Price'))
    value = models.PositiveIntegerField(_('Value'))
    published = models.BooleanField(_('Published'), default=False)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    description = models.TextField(_('description'),)
    image = models.ImageField(_('image'), upload_to='products/%Y/%m/%d/')
    image_base64 = models.TextField(default=None, null=True, blank=True)
    product = models.ForeignKey(
        'shop.Product',
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name=_('product')
    )

    class Meta:
        verbose_name = _('ProductImage')
        verbose_name_plural = _('ProductImages')

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
        verbose_name=_('user')
    )
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        verbose_name = _('Basket')
        verbose_name_plural = _('Baskets')


class BasketItem(models.Model):
    basket = models.ForeignKey(
        'shop.Basket',
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name=_('basket')
    )
    product = models.ForeignKey(
        'shop.Product',
        on_delete=models.CASCADE,
        verbose_name=_('product')
    )
    count = models.PositiveSmallIntegerField(_('count'), default=1)

    class Meta:
        verbose_name = _('BasketItem')
        verbose_name_plural = _('BasketItems')

    def __str__(self):
        return f'{self.product}: {self.count}'


class Order(models.Model):
    WAITING = _('Waiting')
    PROCESSING = _('Processing')
    PROCESSED = _('Processed')
    ORDER_STATUS = (
        (WAITING, WAITING),
        (PROCESSING, PROCESSING),
        (PROCESSED, PROCESSED)
    )

    basket = models.ForeignKey(
        'shop.Basket',
        on_delete=models.CASCADE,
        verbose_name=_('basket')
    )
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUS,
        default=WAITING,
        verbose_name=_('status')
    )
    address = models.TextField(_('address'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class RequestError(models.Model):
    exception_name = models.CharField(_('exception_name'), max_length=50)
    exception_value = models.CharField(_('exception_value'), max_length=250)
    exception_tb = models.TextField(_('exception_tb'))
    request_method = models.CharField(_('Request_method'), max_length=10)
    path = models.CharField(_('path'), max_length=500)
    query = JSONField(_('query'))
    data = JSONField(_('data'))
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )
        verbose_name = _('RequestError')
        verbose_name_plural = _('RequestErrors')

    def __str__(self):
        return f'{self.exception_name}: {self.exception_value}'
