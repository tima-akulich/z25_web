from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from shop.models import Category, CategoryTranslation, Product, ProductImage



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
        UserModel = get_user_model()
        self.user = UserModel.objects.filter(username=data['username']).first()
        if not self.user or not self.user.check_password(data['password']):
            raise serializers.ValidationError('Invalid credentials')
        return data

    def save(self, **kwargs):
        token, _ = Token.objects.get_or_create(user=self.user)
        self._data['key'] = token.key


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email', 'is_staff']


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'auth_token')
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = 'images'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(ProductSerializer):
    product = ProductImageSerializer(many=True, read_only=True)

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + 'images'
