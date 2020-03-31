from django.contrib import admin
from .models import Product
from .models import Basket
from .models import Category
from .models import ProductImage
from .models import BasketItem


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('description', 'image')
    extra = 0
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'price', 'amount', '__str__', 'id')
    search_fields = ('title', 'number')
    list_display_links = ('__str__', 'id')
    list_editable = ('number', 'title')
    list_filter = ('title', 'price', 'amount')
    sortable_by = ('price', 'amount')
    inlines = (ProductImageInline,)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_subcategories')
    filter_horizontal = ('subcategories', )

    def get_subcategories(self, obj):
        subcategories = obj.subcategories.all().values_list('title', flat=True)
        return ', '.join(subcategories)
    get_subcategories.short_description = 'Subcategories'


class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', '__str__', 'status')
    search_fields = ('user', 'number')


class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'count')
    list_display_links = ('product', 'count')




admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(BasketItem, BasketItemAdmin)
