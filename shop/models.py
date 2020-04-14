import base64

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _, get_language


class ModelTranslation(models.Model):
    __item_class__ = None

    lang = models.CharField(
        _('Lang'),
        max_length=10,
        choices=settings.LANGUAGES
    )
    title = models.CharField(
        _('Title'),
        max_length=100
    )

    class Meta:
        abstract = True
        unique_together = (
            ('lang', 'item'),
        )


class LocalizationMixin:
    @property
    def localization(self):
        translations = dict(self.translations.all().values_list(
            'lang', 'title'))
        lang = get_language()
        return translations.get(lang) or self.id


class Category(LocalizationMixin, models.Model):
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


class CategoryTranslation(ModelTranslation):
    item = models.ForeignKey(
        'shop.Category',
        on_delete=models.CASCADE,
        related_name='translations'
    )


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

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
        on_delete=models.SET_NULL,
        related_name='baskets'
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
        (WAITING, _('Waiting')),
        (PROCESSING, _('Processing')),
        (PROCESSED, _('Processed'))
    )

    basket = models.ForeignKey(
        'shop.Basket',
        on_delete=models.CASCADE,
        related_name='orders'
    )
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
