from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Home.as_view(),name= "home"),
    path('musicians/',views.MusicianListView.as_view(),name = 'musicianlist-view'),
    path('musicians/<int:pk>/',views.MusicianView.as_view(),name = 'musician-view'),
    path('albums/',views.AlbumListView.as_view(),name = 'musicianlist-view'),
    path('albums/<int:pk>/',views.AlbumView.as_view(),name = 'musician-view'),
   
    
]