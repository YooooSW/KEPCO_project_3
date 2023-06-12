
from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    ### http://127.0.0.1:8000/
    path('', views.index),
    ### http://127.0.0.1:8000/index
    path('index/', views.index),
    path('', include('mainapp.urls')),
    path('admin/', admin.site.urls),
]
