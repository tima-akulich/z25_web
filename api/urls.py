from django.urls import path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from api.views import CategoryViewSet, LoginApiView, SignUpApiView, ProductListView
from api.views import BasketDetailsView, BasketItemViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
# router.register('basket/items', BasketItemViewSet, basename='items')

urlpatterns = [
    # path('categories', CategoryListCreateView.as_view(), name='categories.list'),
    # path('categories/<int:pk>', CategoryDetailsView.as_view(), name='category.details'),
    path('login', LoginApiView.as_view(), name='login'),
    path('signup', SignUpApiView.as_view(), name='signup'),
    path('products', ProductListView.as_view(), name='products_list'),
    path('categories/<int:pk>/products', ProductListView.as_view(), name='products_by_category'),
    path('basket', BasketDetailsView.as_view(), name='basket'),
    path('schema', get_schema_view(
        title='Shop API',
        description='Api for amazing shop',
        version='v1'
    ), name='api-schema'),
    path('swagger', TemplateView.as_view(
        template_name='swagger.html'
    ), name='swagger-api'),
    path('redoc', TemplateView.as_view(
        template_name='redoc.html'
    ), name='redoc-api')
] + router.urls
