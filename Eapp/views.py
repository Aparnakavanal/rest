from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework import generics
from .models import Items,Orders
from .serializers import Itemserializer
from Euser .serializers import OrderCreateSerializers


class ItemList(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = Itemserializer

class DetailMixin(generics.GenericAPIView,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin) :
    queryset = Items.objects.all()
    serializer_class = Itemserializer


    def get(self,request,*args,**kwargs):
        return self.retrieve(*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.delete(*args,**kwargs)

class ItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = Itemserializer

class ViewOrder(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderCreateSerializers
