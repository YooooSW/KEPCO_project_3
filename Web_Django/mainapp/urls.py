from django.urls import path

### from 뒤에 작성규칙
#  - 폴더 경로 또는 폴더 경로 + 파일명
###

from . import views

urlpatterns = [

    ### http://127.0.0.1:8000/sprint/index
    path('', views.index),
    path('index/', views.index),
    path('Create_Posts_page/', views.Create_Posts_page),
    path('car_repair_calculation_Page/', views.car_repair_calculation_Page),
    path('car_repair_calculation/', views.car_repair_calculation),
    path('load_view/', views.car_repair_price),
    path('test/', views.test),
    

    
]
