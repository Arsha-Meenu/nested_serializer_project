import imp
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.


# Create your views here.
class Home(APIView):
    def get(self,request):
        return HttpResponse("started nested serializer of api 2.")


class MusicianListView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()

class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

