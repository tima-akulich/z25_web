from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, LoginApiView

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [
    # path('categories', CategoryListCreateView.as_view(), name='categories.list'),
    # path('categories/<int:pk>', CategoryDetailsView.as_view(), name='category.details'),
    path('login', LoginApiView.as_view(), name='login')
] + router.urls
