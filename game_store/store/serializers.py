from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Product

UserModel = get_user_model()

class UserSerializer(serializers.Serializer):
    class Meta:
        model = UserModel
        exclude = ['password']

    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validation_data):
        pass

    def update(self, instance, validated_data):
        pass


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'desc', 'thumb', 'image1', 'image2', 'category']

