from django.urls import path
from .views import ListView,IndexView,DetailedView,AddToCartView,CartView,RemoveView,LoginView,OrderPro

urlpatterns = [
    path("l1",ListView.as_view(),name="l1"),
    path("l2",IndexView.as_view(),name="l2"),
    path("de/<int:pk>",DetailedView.as_view(),name="de"),
    path("add/<int:id>",AddToCartView.as_view(),name="add"),
    path("cart",CartView.as_view(),name="cart"),
    path("remove/<int:pk>",RemoveView.as_view(),name="remove"),
    path("login",LoginView.as_view(),name="login"),
    path("op",OrderPro.as_view(),name="op")

]