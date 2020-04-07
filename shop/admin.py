from django.contrib import admin  # noqa

from shop.models import Product
from shop.models import Category
from shop.models import ProductImage
from shop.models import Order

from shop.models import RequestError


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_subcategories')
    filter_horizontal = ('subcategories', )

    def get_subcategories(self, obj):
        subcategories = obj.subcategories.all().values_list('title', flat=True)
        return ', '.join(subcategories)
    get_subcategories.short_description = 'Subcategories'


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('description', 'image', 'image_base64')
    extra = 0
    min_num = 1
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    inlines = (ProductImageInline, )


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
    list_display = (
        'basket',
        'status',
        'address',
        'created_at',
        'updated_at'
    )
    list_filter = ('basket', 'address', 'created_at')
    search_fields = ('address', 'created_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RequestError, RequestErrorAdmin)
admin.site.register(Order, OrderAdmin)

