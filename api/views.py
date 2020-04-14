from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from api.permissions import IsAdminOrReadOnly
from api.serializers import CategorySerializer, CategoryDetailsSerializer, LoginSerializer
from api.serializers import ProductListSerializer, UserSerializer, BasketEditSerializer
from shop.models import Category, Product, Order, Basket
from rest_framework.permissions import IsAuthenticated
from api.serializers import OrderEditSerializer
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


class ProductApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]


class UserAuthenticationApiView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class BasketCreateApi(CreateAPIView):
    serializer_class = BasketEditSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        basket = Basket.objects.filter(
                user=self.request.user
            ).prefetch_related('items').latest('updated_at')
        return basket


class OrderCreateApi(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderEditSerializer
    permission_classes = [IsAuthenticated]
