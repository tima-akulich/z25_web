from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import BasketCreateApi, OrderCreateApi
from api.views import CategoryViewSet, LoginApiView, ProductApiView, UserAuthenticationApiView

router = DefaultRouter()
router.register('categories/', CategoryViewSet, basename='category')


from api.views import CategoryViewSet, LoginApiView

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    # path('categories', CategoryListCreateView.as_view(), name='categories.list'),
    # path('categories/<int:pk>', CategoryDetailsView.as_view(), name='category.details'),
    path('login', LoginApiView.as_view(), name='login'),
    path('products/', ProductApiView.as_view()),
    path('users/create/', UserAuthenticationApiView.as_view()),
    path('baskets/create', BasketCreateApi.as_view()),
    path('orders/create', OrderCreateApi.as_view())
] + router.urls

   