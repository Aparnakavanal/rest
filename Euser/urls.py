from django.urls import path
from .views import ListView,IndexView,DetailedView,AddToCartView,CartView,RemoveView,LoginView,OrderPro

urlpatterns = [
    path("listview",ListView.as_view(),name="listview"),
    path("indexview",IndexView.as_view(),name="indexview"),
    path("detailedview/<int:pk>",DetailedView.as_view(),name="detailedview"),
    path("addtocart/<int:id>",AddToCartView.as_view(),name="addtocart"),
    path("cartview",CartView.as_view(),name="cartview"),
    path("removeview/<int:pk>",RemoveView.as_view(),name="removeview"),
    path("loginview",LoginView.as_view(),name="loginview"),
    path("orderpro",OrderPro.as_view(),name="orderpro")

]