from rest_framework import serializers
from .models import Items,Category

class Itemserializer(serializers.ModelSerializer):
    class Meta:
        model=Items
        fields="__all__"