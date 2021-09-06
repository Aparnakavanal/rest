from rest_framework import serializers
from .models import Book
from rest_framework .serializers import ModelSerializer


class BookSerializer(serializers.Serializer):
    book_name=serializers.CharField()
    author=serializers.CharField()
    pages=serializers.CharField()
    price=serializers.CharField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.book_name=validated_data.get("book_name",instance.book_name)
        instance.author=validated_data.get("author",instance.author)
        instance.pages = validated_data.get("pages",instance.pages)
        instance.price= validated_data.get("price",instance.price)
        instance.save()
        return instance

class BookModelSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields=["id","book_name","author","pages","price"]

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()