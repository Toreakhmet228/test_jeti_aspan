from rest_framework import serializers
from .models import City, CustomUser, Store, Product, ProductImage

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class CustomUserSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'image', 'city']


class StoreSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Store
        fields = ['id', 'name', 'city']


class ProductImageSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'city']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    store = StoreSerializer()
    city = CitySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'images', 'city', 'store', 'stock', 'view_count']


class ProductDetailSerializer(ProductSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'images', 'city', 'store', 'stock', 'view_count']
