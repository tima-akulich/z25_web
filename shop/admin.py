from django.contrib import admin
from shop.models import (Product, Company, Customer, Order)

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Product Attributes', {'fields': ('name', 'company', 'category')}),
        ('Warehouse Information', {'fields': ('quantity', 'number')})
    )
    search_fields = ['name', 'number']
    list_display = ['name', 'number', 'quantity', 'company', 'category']
    list_filter = ('number', 'name', 'company')
    radio_fields = {'category': admin.HORIZONTAL,
                    'company': admin.HORIZONTAL}


class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_filter = ('name',)


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {'fields': ('first_name', 'last_name', 'address')}),
        ('Contact Information', {'fields': ('email',),
                                 'classes': ('collapse',)})
    )
    search_fields = ['last_name', 'email', 'address']
    list_filter = ('last_name', 'email', 'address')
    list_display = ['first_name', 'last_name', 'address', 'email']


class OrderAdmin(admin.ModelAdmin):
    fields = ('product_name', 'customer_name', 'quantity')
    search_fields = ['product_name', 'customer_name']
    list_display = ['product_name', 'customer_name', 'quantity']


admin.site.register(Product, ProductAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
