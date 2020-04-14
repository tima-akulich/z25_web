from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from shop.models import Category, CategoryTranslation
from shop.models import Product
from shop.models import BasketItem
from shop.models import Order
from shop.models import Category, CategoryTranslation
User = get_user_model()


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


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self._data = {}

    def validate(self, data):
        self.user = User.objects.filter(username=data['username']).first()

        if not self.user or not self.user.check_password(data['password']):
            raise serializers.ValidationError('Invalid credentials')
        return data

    def save(self, **kwargs):
        token, _ = Token.objects.get_or_create(user=self.user)
        self._data['key'] = token.key


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'categories', 'price', 'value', 'published')


class UserSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        if validated_data['password1'] != validated_data['password2']:
            user.delete()
            raise serializers.ValidationError('Incorrect Password!')
        else:
            user.set_password(validated_data['password1'])
            user.save()
        return user

    class Meta:
        model = User
        fields = ("id", "username", "password1", 'password2', 'email')


class BasketEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = '__all__'


class OrderEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('address', 'basket')

