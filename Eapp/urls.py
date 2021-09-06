from django.urls import path
from .views import ItemList,DetailMixin,ItemView,ViewOrder


urlpatterns=[
    path("itemlist",ItemList.as_view(),name="itemlist"),
    path("detail",DetailMixin.as_view(),name="detail"),
    path("itemview/<int:pk>",ItemView.as_view(),name="itemview"),
    path("vieworder",ViewOrder.as_view(),name="vieworder")

]