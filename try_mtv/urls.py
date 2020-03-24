from django.urls import path
from try_mtv.views import check_parentheses


urlpatterns = [
    path('check', check_parentheses, name='check_parentheses'),
]
