
from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('', include('mainapp.urls')),
    path('admin/', admin.site.urls),
]
