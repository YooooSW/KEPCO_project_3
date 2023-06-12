from django.urls import path

### from 뒤에 작성규칙
#  - 폴더 경로 또는 폴더 경로 + 파일명
###

from . import views

urlpatterns = [

    ### http://127.0.0.1:8000/index
    path('', views.index),
    path('index/', views.index),

    path('Create_Posts_page/', views.Create_Posts_page),

    path('login_form1/', views.login_form1),
    # sns로그인 폼 연결
    ### http://127.0.0.1:8000/sns_login_form
    path('sns_login_form/', views.slogin_form),

    ### http://127.0.0.1:8000/login_form
    path('login_form/', views.login_form),
    

    
]
