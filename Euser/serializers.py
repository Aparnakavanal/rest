from rest_framework import serializers
from Eapp.models import Orders,Items,Mycart

class LoginSerializers(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

class AddToCartSerializers(serializers.ModelSerializer):
    class Meta:
        model=Items
        fields=["id"]

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model=Mycart
        fields="__all__"

class OrderCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields="__all__"