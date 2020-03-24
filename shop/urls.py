from django.urls import path
from shop.views import (
    hello_world,
    hello_world_template,
    products,
    product_information
)


urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('template/', hello_world_template, name='template'),
    path('products/', products, name='product_list'),
    path('productinfo', product_information, name='prod_info')
]
