from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api/',include('api.urls')),
    path('api2/',include('api2.urls')),
    path('admin/', admin.site.urls),
]
