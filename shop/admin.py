from django.contrib import admin  # noqa

from shop.models import Product
from shop.models import Category
from shop.models import ProductImage
from shop.models import Error505

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


<<<<<<< HEAD
class Error505Admin(admin.ModelAdmin):
    list_display = ('status_code', 'body', 'time_period')
=======
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
>>>>>>> d7cffe717e0a719dd5bf666ed4c3b6acbd90c6d0


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
<<<<<<< HEAD
admin.site.register(Error505, Error505Admin)
=======

admin.site.register(RequestError, RequestErrorAdmin)
>>>>>>> d7cffe717e0a719dd5bf666ed4c3b6acbd90c6d0
