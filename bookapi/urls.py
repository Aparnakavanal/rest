from django.urls import path
from .views import book_list,book_details,Books,BookDetails,BookList,BookDetailsMixin,LoginView
from django.views.generic import TemplateView

urlpatterns=[
    path("mybook",TemplateView.as_view(template_name="index.html"),name="mybook"),
    path("books",book_list,name="books"),
    path("books/<int:id>",book_details,name="details"),
    path("cbooks",Books.as_view(),name="cbooks"),
    path("cbooks/<int:pk>",BookDetails.as_view(),name="details"),
    path("mbooks",BookList.as_view(),name="mlist"),
    path("mbooks/<int:pk>",BookDetailsMixin.as_view(),name="mdetail"),
    path("login",LoginView.as_view(),name="login")

]