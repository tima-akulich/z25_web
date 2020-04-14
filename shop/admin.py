from django.contrib import admin  # noqa
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext
from django.conf import settings

from shop.models import Product, Order
from shop.models import Category
from shop.models import ProductImage
from shop.models import CategoryTranslation

from shop.models import RequestError


class CategoryTranslationAdmin(admin.TabularInline):
    model = CategoryTranslation
    fields = ('lang', 'title')
    max_num = len(settings.LANGUAGES)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_subcategories')
    filter_horizontal = ('subcategories', )
    inlines = (CategoryTranslationAdmin, )

    def get_subcategories(self, obj):
        subcategories = obj.subcategories.all().values_list('title', flat=True)
        return ', '.join(subcategories)
    get_subcategories.short_description = 'Subcategories'


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('description', 'image', 'image_base64')
    extra = 0
    min_num = 0
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    inlines = (ProductImageInline, )
    list_display = ('__str__', 'published')


class RequestErrorAdmin(admin.ModelAdmin):
    list_display = (
        'exception_name',
        'exception_value',
        'request_method',
        'path',
        'created_at'
    )
    list_filter = ('exception_name', 'request_method', 'created_at')
    search_fields = ('exception_name', 'exception_value', 'path')
    readonly_fields = (
        'exception_name',
        'exception_value',
        'exception_tb',
        'query',
        'data',
        'request_method',
        'path',
        'created_at'
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'address')
    readonly_fields = ('basket', 'get_ordered_products', 'get_products_count')

    def get_user(self, obj):
        return obj.basket.user
    get_user.short_description = 'User'

    def get_ordered_products(self, obj):
        result = ''
        for item in obj.basket.items.all():
            result += f'<strong>{item.product}</strong>: {item.count}<br>'
        return mark_safe(result)
    get_ordered_products.short_description = 'Products'

    def get_products_count(self, obj):
        count = obj.basket.items.all().count()
        return ngettext(
            '%(items_count)s product', '%(items_count)s products', count
        ) % {
            'items_count': count
        }
    get_products_count.short_description = _('Количество продуктов')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(RequestError, RequestErrorAdmin)

admin.site.register(Order, OrderAdmin)
