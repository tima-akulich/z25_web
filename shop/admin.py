from django.contrib import admin
from .models import Product
from .models import Basket
from .models import BasketElements


class ProductAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'price', 'amount', '__str__', 'id')
    search_fields = ('title', 'number')
    list_display_links = ('__str__', 'id')
    list_editable = ('number', 'title')
    list_filter = ('title', 'price', 'amount')
    sortable_by = ('price', 'amount')


class BasketAdmin(admin.ModelAdmin):
    list_display = ('number', 'user', '__str__', 'status', 'id')
    search_fields = ('user', 'number')
    list_display_links = ('__str__', 'id')


class BasketElementsAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id')
    search_fields = ('user', 'element')
    list_display_links = ('__str__', 'id')



admin.site.register(Product, ProductAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketElements, BasketElementsAdmin)

