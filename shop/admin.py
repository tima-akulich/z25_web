from django.contrib import admin  # noqa

from shop.models import Product
from shop.models import Category
from shop.models import ProductImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_subcategories')
    filter_horizontal = ('subcategories', )

    def get_subcategories(self, obj):
        subcategories = obj.subcategories.all().values_list('title', flat=True)
        return ', '.join(subcategories)
    get_subcategories.short_description = 'Subcategories'


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('description', 'image')
    extra = 0
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    inlines = (ProductImageInline, )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
