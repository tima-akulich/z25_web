from django.urls import path
from django.conf import settings

from shop.views import products_list_view
from shop.views import product_details_view
from shop.views import try_forms
from shop.views import index, categories, products_by_category

from django.conf.urls.static import static


urlpatterns = [
    path('forms', try_forms, name='try_forms'),
    path('', index, name='products'),
    path('product/<str:pk>', product_details_view, name='product_details'),
    path('products/', products_list_view, name='product_list'),
    path('categories/', categories, name='categories'),
    path('categories/', products_by_category, name='prods_by_cat')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
