from django.urls import path
from django.urls import include
from django.urls import re_path as url
# from auth.apis import (
#     LoginApi, 
#     LogoutApi, 
#     GoogleLoginApi, 
#     GoogleSigninCallBackApi
# )
# from auth.googleapi import *

### from 뒤에 작성규칙
#  - 폴더 경로 또는 폴더 경로 + 파일명
###

from . import views

# login_patterns = [
#     path('google', GoogleLoginApi.as_view(), name='google_login'),
#     path('google/callback', GoogleSigninCallBackApi.as_view(), name='google_login_callback'),
# ]


urlpatterns = [

    ### http://127.0.0.1:8000/index
    path('', views.index),
    path('index/', views.index),

    path('Create_Posts_page/', views.Create_Posts_page),

    path('car_repair_calculation_Page/', views.car_repair_calculation_Page),
    path('car_repair_price/', views.car_repair_price, name='car_repair_price'),

    
    # path('test/', views.test),
    path('login_form1/', views.login_form1),
    # sns로그인 폼 연결
    ### http://127.0.0.1:8000/sns_login_form
    path('sns_login_form/', views.slogin_form),
    ### http://127.0.0.1:8000/sns_login_form
    path('sns_login_form/account/', views.slogin_form),
    # path('logout', LogoutApi.as_view(), name="logout"),
    # path('login/', include(login_patterns)),

    ### http://127.0.0.1:8000/login_form
    path('login_form/', views.login_form),

    ### http://127.0.0.1:8000/search_id
    path('search_id/', views.search_id),

    ### http://127.0.0.1:8000/search_pwd
    path('search_pwd/', views.search_pwd),

    ### http://127.0.0.1:8000/sign_up
    path('sign_up/', views.sign_up),

    ### http://127.0.0.1:8000/board
    path('board/', views.board),
]

