from datetime import timedelta

import requests
from django.contrib.auth import get_user_model
from django.http import Http404
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from amazing_shop import settings
from shop.models import Category, CategoryTranslation, Product, ProductImage, \
    BasketItem, Basket, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')


class CategoryTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTranslation
        fields = ('lang', 'title')


class CategoryDetailsSerializer(CategorySerializer):
    translations = CategoryTranslationSerializer(many=True, read_only=True)

    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + ('translations', )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'description', 'image', 'product')


class ProductSerializer(serializers.ModelSerializer):
    categories = CategoryDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'categories', 'price', 'value', 'published')


class ProductDetailsSerializer(ProductSerializer):
    image = ProductImageSerializer

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ('image',)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self._data = {}

    def validate(self, data):
        UserModel = get_user_model()
        self.user = UserModel.objects.filter(username=data['username']).first()
        if not self.user or not self.user.check_password(data['password']):
            raise serializers.ValidationError('Invalid credentials')
        return data

    def save(self, **kwargs):
        token, _ = Token.objects.get_or_create(user=self.user)
        self._data['key'] = token.key


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = {}

    def save(self, **kwargs):
        get_user_model().objects.create_user(
            username=self.validated_data['username'],
            password=self.validated_data['password'],
            email=self.validated_data['email']
        )
        resp = requests.post(
            r'http://127.0.0.1:8000/ru/api/login',
            json={
                'username': self.validated_data['username'],
                'password': self.validated_data['password']
            }
        ).json()
        self._data.update(**self.validated_data, **resp)
        self._data.pop('password')

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')


class BasketItemSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        basket = last_basket(user)
        basket_item = BasketItem.objects.create(
            basket=basket,
            product=validated_data['product'],
            count=validated_data['count']
        )
        return basket_item

    class Meta:
        model = BasketItem
        fields = ('id', 'product', 'count')


class OrderSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        basket = last_basket(user)
        order = None
        if basket.items.all():
            order = Order.objects.create(
                basket=basket,
                address=validated_data['address']
            )
        if order is None:
            raise Http404
        Basket.objects.create(user=user)
        return order

    class Meta:
        model = Order
        fields = ('id', 'address')


def last_basket(user):
    Basket.objects.filter(
        user=user,
        updated_at__lt=timezone.now() - timedelta(
            days=settings.BASKET_STORE_DAYS
        )
    ).delete()
    basket = None
    try:
        basket = Basket.objects.filter(
            user=user
        ).latest('updated_at')
    except Basket.DoesNotExist:
        basket = Basket.objects.create(user=user)
    return basket
