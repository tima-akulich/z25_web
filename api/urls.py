from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, LoginApiView, CreateUserView, \
    ProductViewSet, ProductImageViewSet, BasketItemCreateView, OrderCreateView

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('product-images', ProductImageViewSet, basename='product-image')
router.register('createuser', CreateUserView)

urlpatterns = [
    # path('categories', CategoryListCreateView.as_view(), name='categories.list'),
    # path('categories/<int:pk>', CategoryDetailsView.as_view(), name='category.details'),
    path('login', LoginApiView.as_view(), name='login'),
    path('basket-items', BasketItemCreateView.as_view(), name='basket-item'),
    path('orders', OrderCreateView.as_view(), name='order'),
] + router.urls
