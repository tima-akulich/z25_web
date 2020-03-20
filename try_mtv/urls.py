from django.urls import path
from try_mtv.views import hello_world, is_correct

urlpatterns = [
    path('hello', hello_world, name='hello_world'),
    path('template', is_correct, name='is_correct')
]