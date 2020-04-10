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

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    description = models.TextField(_('Description'))
    image = models.ImageField(_('Image'), upload_to='products/%Y/%m/%d/')
    image_base64 = models.TextField(default=None, null=True, blank=True)
    product = models.ForeignKey(
        'shop.Product',
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name=_('Product')
    )

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')

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
    created_at = models.DateTimeField(_('Created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated_at'), auto_now=True)

    class Meta:
        verbose_name = _('Basket')
        verbose_name_plural = _('Baskets')


class BasketItem(models.Model):
    basket = models.ForeignKey(
        'shop.Basket',
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name=_('Basket')
    )
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, verbose_name=_('Product'))
    count = models.PositiveSmallIntegerField(_('Count'), default=1)

    class Meta:
        verbose_name = _('Basket Item')
        verbose_name_plural = _('Basket Items')

    def __str__(self):
        return f'{self.product}: {self.count}'


class Order(models.Model):
    WAITING = _('waiting')
    PROCESSING = _('processing')
    PROCESSED = _('processed')
    ORDER_STATUS = (
        (WAITING, WAITING.title()),
        (PROCESSING, PROCESSING.title()),
        (PROCESSED, PROCESSED.title())
    )

    basket = models.ForeignKey('shop.Basket', on_delete=models.CASCADE, verbose_name=_('Basket'))
    created_at = models.DateTimeField(_('Created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated_at'), auto_now=True)
    status = models.CharField(
        _('Status'),
        max_length=10,
        choices=ORDER_STATUS,
        default=WAITING
    )
    address = models.TextField(_('Address'))

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class RequestError(models.Model):
    exception_name = models.CharField(_('Exception_name'), max_length=250)
    exception_value = models.CharField(_('Exception_value'), max_length=250)
    exception_tb = models.TextField(_('Exception_tb'))
    request_method = models.CharField(_('Request_method'), max_length=10)
    path = models.CharField(_('Path'), max_length=500)
    query = JSONField(_('Query'))
    data = JSONField(_('Data'))
    created_at = models.DateTimeField(_('Created_at'), auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )
        verbose_name = _('RequestError')
        verbose_name_plural = _('RequestErrors')

    def __str__(self):
        return f'{self.exception_name}: {self.exception_value}'

