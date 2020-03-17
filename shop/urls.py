from django.urls import path
from shop.views import hello_world
from shop.views import hello_world_template


urlpatterns = [
    path('hello', hello_world, name='hello_world'),
    path('template', hello_world_template, name='template')
]
