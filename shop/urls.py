from django.urls import path
from django.conf import settings
from django.views.generic import TemplateView

from shop.views import product_details_view
from shop.views import category_root_view
from shop.views import TryCBV
from shop.views import ProductsList
from shop.views import ProductDetail
from shop.views import ProductFormView

from django.conf.urls.static import static


urlpatterns = [
    path('cbv', TryCBV.as_view(), name='try_cbv'),
    path('cbv1', TemplateView.as_view(template_name='try_cbv.html'), name='try_cbv'),
    path('form', ProductFormView.as_view(), name='product_form'),
    path('', ProductsList.as_view(), name='products'),
    path('product/<str:pk>', ProductDetail.as_view(), name='product_details'),
    path('category/', category_root_view, name='categories_list'),
    path('category/<slug:category>', ProductsList.as_view(), name='products_by_category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
