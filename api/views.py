from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, \
    AllowAny
from django.contrib.auth.models import User

from api.permissions import IsAdminOrReadOnly
from api.serializers import CategorySerializer, CategoryDetailsSerializer, LoginSerializer, UserSerializer, CreateUserSerializer, ProductSerializer

from shop.models import Category, Product


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


# class LoginApiView(CreateAPIView):
#     serializer_class = LoginSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny,)
        return super(UserViewSet, self).create(request, *args, **kwargs)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]