from django.urls import path
from . import views
from shop.views import products_details_view
from shop.views import try_forms
from django.conf import settings
from shop.views import products_list_view
from shop.views import hello_list
from shop.views import categories_view


from django.conf.urls.static import static


urlpatterns = [
    path('forms', try_forms, name='try_forms'),
    path('products', products_list_view, name='products'),
    path('product/<str:pk>', products_details_view, name='product_details'),
    path('hello', hello_list, name='hello_list'),
    path('categories/', products_list_view, name='categories'),
    path('<slug:category>', products_list_view, name='products_by_category'),
    path('categories/<slug:category>', categories_view, name='categories_by_category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

