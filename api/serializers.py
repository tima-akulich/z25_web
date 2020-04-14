from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from shop.models import Category, CategoryTranslation, Product, ProductImage, \
    Basket, BasketItem

UserModel = get_user_model()


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


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self._data = {}

    def get_user(self):
        return self.user

    def save(self, **kwargs):
        token, _ = Token.objects.get_or_create(user=self.get_user())
        self._data['key'] = token.key


class LoginSerializer(AuthSerializer):
    def validate(self, data):
        self.user = UserModel.objects.filter(username=data['username']).first()
        if not self.user or not self.user.check_password(data['password']):
            raise serializers.ValidationError('Invalid credentials')
        return data


class SignUpSerializer(AuthSerializer):
    def get_user(self):
        return UserModel.objects.create_user(**self.validated_data)


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ('description', 'image')

    def get_image(self, obj):
        return obj.image.url


class ProductSerializer(serializers.ModelSerializer):
    categories = CategoryDetailsSerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title', 'images', 'categories',
            'price', 'value', 'created_at', 'updated_at'
        )


class BasketItemCreateSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(required=True)

    class Meta:
        model = BasketItem
        fields = ('product_id', 'count')

    def create(self, validated_data):
        validated_data['basket_id'] = self.context['basket_id']
        return super().create(validated_data)


class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = BasketItem
        fields = ('id', 'product', 'count')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class BasketDetailsSerializer(serializers.ModelSerializer):
    items = BasketItemSerializer(many=True)

    class Meta:
        model = Basket
        fields = ('id', 'user', 'updated_at', 'items')
