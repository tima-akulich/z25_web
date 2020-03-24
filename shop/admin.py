from django.contrib import admin
from shop.models import Product
from shop.models import Manufacturer
from shop.models import Category
from shop.models import Order


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category', 'price', 'manufacturer')
    search_fields = ('title', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Order)