from contextlib import suppress

from django.utils.functional import cached_property
from rest_framework.generics import CreateAPIView, ListAPIView, \
    RetrieveAPIView, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsAdminOrReadOnly
from api.serializers import CategoryDetailsSerializer, LoginSerializer, \
    SignUpSerializer, ProductSerializer, BasketDetailsSerializer, \
    BasketItemCreateSerializer, BasketItemSerializer
from shop.models import Category, Product, Basket, BasketItem


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


class SignUpApiView(CreateAPIView):
    serializer_class = SignUpSerializer


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(
        published=True
    ).prefetch_related('categories')
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.kwargs.get('pk'):
            queryset = queryset.filter(categories__pk=self.kwargs['pk'])
        return queryset


class BasketDetailsView(RetrieveAPIView):
    serializer_class = BasketDetailsSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return get_object_or_404(
            Basket.objects.prefetch_related('items').latest('updated_at'),
            user=self.request.user
        )


class BasketItemViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = BasketItemSerializer

    @cached_property
    def basket(self):
        return get_object_or_404(
            Basket.objects.prefetch_related('items').latest('updated_at'),
            user=getattr(self.request, 'user', None)
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['basket_id'] = getattr(self.basket, 'id', None)
        return context

    def get_serializer_class(self):
        if getattr(self.request, 'method', 'GET') == 'POST':
            return BasketItemCreateSerializer
        return BasketItemSerializer

    def get_queryset(self):
        return BasketItem.objects.filter(
            basket=self.basket
        )
