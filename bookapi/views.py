from django.shortcuts import render
from .serializers import BookSerializer,BookModelSerializer,LoginSerializer
from .models import Book
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from  rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import authentication
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
@csrf_exempt
def book_list(request):
    if request.method=='GET':
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="POST":
        data=JSONParser().parse(request)
        serializer=BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return  JsonResponse(serializer.errors,status=400)
#
#
@csrf_exempt
def book_details(request,*args,**kwargs):
    try:
        book=Book.objects.get(id=kwargs.get("id"))
    except:
        msg="not exist"
        return JsonResponse(data=msg,status=400,safe=False)
    if request.method=="GET":
        serializer=BookSerializer(book)
        return JsonResponse(serializer.data,status=200)
    elif request.method=="PUT":
        data=JSONParser().parse(request)
        serializer=BookSerializer(instance=book,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        else:
            return JsonResponse(serializer.errors,status=400)
    elif request.method=="DELETE":
        book.delete()
        msg="deleted"
        return JsonResponse(data=msg,status=200,safe=False)

class Books(APIView):
    def get(self,request):
        books=Book.objects.all()
        serializer=BookModelSerializer(books,many=True)
        return Response(serializer.data,status=200)

    def post(self,request):
        serializer=BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BookDetails(APIView):
    def get_object(self,pk):
        try:
            return Book.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,*args,**kwargs):
        book=self.get_object(kwargs.get("pk"))
        serializer=BookModelSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        book=self.get_object(kwargs.get("pk"))
        serializer=BookModelSerializer(instance=book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,**kwargs):
        book=self.get_object(kwargs.get("pk"))
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filterset_fields=['book_name']

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class BookDetailsMixin(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    authentication_classes = [authentication.TokenAuthentication,authentication.BasicAuthentication]
    parser_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class LoginView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                token,created=Token.objects.get_or_create(user=user)
            return Response({"token":token.key},status=status.HTTP_201_CREATED)












