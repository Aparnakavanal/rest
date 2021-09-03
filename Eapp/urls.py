from django.urls import path
from .views import ItemList,DetailMixin,ItemView,ViewOrder


urlpatterns=[
    path("li",ItemList.as_view(),name="li"),
    path("detail",DetailMixin.as_view(),name="detail"),
    path("iv/<int:pk>",ItemView.as_view(),name="iv"),
    path("ov",ViewOrder.as_view(),name="ov")

]