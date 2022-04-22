from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Home.as_view(),name= "home"),
    path('test/',views.BookView.as_view(),name = 'book-view'),
]