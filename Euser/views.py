from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response

from Eapp.models import Mycart,Items,Orders
from Eapp.serializers import Itemserializer
from rest_framework import mixins, status
from rest_framework import generics
from django.contrib.auth import authenticate,login
from rest_framework .views import APIView
from .serializers import CartSerializers,LoginSerializers,OrderCreateSerializers
from rest_framework.authtoken.models import Token


# Create your views here.
class ListView(generics.GenericAPIView,
               mixins.ListModelMixin):
    queryset = Items.objects.all()
    serializer_class = Itemserializer
    filterset_fields=["title"]

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
class IndexView(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = Itemserializer

class DetailedView(generics.RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = Itemserializer

class AddToCartView(APIView):
    def post(self, request, *args, **kwargs):
        pid=kwargs.get("id")
        items=Items.objects.get(id=pid)
        user=request.user
        cart=Mycart(product=items,user=user)
        cart.save()
        return Response(status=status.HTTP_200_OK)

class CartView(generics.GenericAPIView,mixins.ListModelMixin):
    queryset = Mycart.objects.filter(status="cart")
    serializer_class = CartSerializers
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class RemoveView(generics.DestroyAPIView):
    queryset = Mycart.objects.all()
    serializer_class = CartSerializers

# class LoginView(APIView):
#     def post(self,request):
#        serializer=LoginSerializers(data=request.data)
#        if serializer.is_valid():
#              username=serializer.validated_data.get("username")
#              password=serializer.validated_data.get("password")
#              user=authenticate(request,username=username,password=password)
#              if user:
#                  token,created=Token.objects.get_or_create(user=user)
#              return Response({"token":token.key},status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            else:
                return Response({"msg":"invalid credentials"})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            # return Response("False")

class OrderPro(APIView):
    qureyset=Mycart.objects.all()
    def post(self,request,format=None):
        serializer=OrderCreateSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # @staticmethod
    # def post(self, request, format=None):
    #     product_id = request.POST.get('product_id', None)
    #     if product_id is not None:
    #         try:
    #             product_obj = Cycle.objects.get(id=product_id)
    #         except Cycle.DoesNotExist:
    #             pass
    #         cart_instance, created = Cart.objects.new_or_get(request)
    #         if product_obj in cart_instance.items.all():
    #             cart_instance.items.remove(product_obj)
    #             added = False
    #         else:
    #             cart_instance.items.add(product_obj)
    #             added = True
    #         request.session['cart_items'] = cart_instance.items.count()
    #         data = {
    #             "added": added,
    #             "removed": not added,
    #             "cartItemCount": cart_instance.items.count()
    #         }
    #         return Response(data, status.HTTP_200_OK)



# class CartViewSet(viewsets.ModelViewSet):
#     queryset = Cart.objects.all().order_by('id')
#     serializer_class = CartSerializer
#
#     @action(methods=['get'], detail=False, url_path='checkout/(?P<userId>[^/.]+)', url_name='checkout')
#     def checkout(self, request, *args, **kwargs):
#
#         try:
#             user = User.objects.get(pk=int(kwargs.get('userId')))
#         except Exception as e:
#             return Response(status=status.HTTP_404_NOT_FOUND,
#                             data={'Error': str(e)})
#
#         cart_helper = CartHelper(user)
#         checkout_details = cart_helper.prepare_cart_for_checkout()
#
#         if not checkout_details:
#             return Response(status=status.HTTP_404_NOT_FOUND,
#                             data={'error': 'Cart of user is empty.'})
#
#         return Response(status=status.HTTP_200_OK, data={'checkout_details': checkout_details})






