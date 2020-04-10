from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from api.permissions import IsAdminOrReadOnly
from api.serializers import CategorySerializer, CategoryDetailsSerializer, LoginSerializer
from shop.models import Category


# class CategoryListCreateView(ListAPIView, CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#     def get_serializer_class(self):
#         if self.request.method == 'post':
#             return CategoryDetailsSerializer
#         return self.serializer_class
#
#
# class CategoryDetailsView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryDetailsSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailsSerializer
    permission_classes = [IsAdminOrReadOnly]


class LoginApiView(CreateAPIView):
    serializer_class = LoginSerializer
