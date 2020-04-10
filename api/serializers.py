from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from shop.models import Category, CategoryTranslation


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
