from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import CategoryViewSet,  UserViewSet, ProductViewSet
from django.conf.urls import url, include
from django.contrib import admin

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    # path('categories', CategoryListCreateView.as_view(), name='categories.list'),
    # path('categories/<int:pk>', CategoryDetailsView.as_view(), name='category.details'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + router.urls
