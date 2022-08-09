from rest_framework import serializers


from .models import *


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class Storeserializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ProductImgserializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'


class Cartserializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class FileUplodedserializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploded
        fields = '__all__'


class Joinserializer(serializers.ModelSerializer):
    product_datails = Productserializer(source='productId')

    class Meta:
        model = CartItem
        fields = '__all__'
