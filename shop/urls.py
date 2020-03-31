from django.urls import path
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

from shop.views import products_list_view
from shop.views import product_details_view
from shop.views import try_forms
from shop.views import base_view
from shop.views import categories_list_view

from django.conf.urls.static import static


urlpatterns = [
    path('forms', try_forms, name='try_forms'),
    path('', base_view, name='products'),
    path('product/<str:pk>', product_details_view, name='product_details'),
    path('products', products_list_view, name='all_products'),
    path('<slug:category>', products_list_view, name='products_by_category'),
    path('cat', categories_list_view, name='categories'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

