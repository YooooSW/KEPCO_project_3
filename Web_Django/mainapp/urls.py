from django.urls import path, include
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
from django.contrib.auth import views as auth_views

# login_patterns = [
#     path('google', GoogleLoginApi.as_view(), name='google_login'),
#     path('google/callback', GoogleSigninCallBackApi.as_view(), name='google_login_callback'),
# ]


urlpatterns = [

    ### http://127.0.0.1:8000/index
    path('', views.index),
    path('index/', views.index),

     ### http://127.0.0.1:8000/login_index
    # path('login_index/', views.login_index),
    
    path('Create_Posts_page/', views.Create_Posts_page),

    path('car_repair_calculation_Page/', views.car_repair_calculation_Page),
    path('car_repair_price/', views.car_repair_price, name='car_repair_price'),

    
    # path('test/', views.test),
    path('login_form1/', views.login_form1),
    # sns로그인 폼 연결 (완료)
    ### http://127.0.0.1:8000/sns_login_form
    path('sns_login_form/', views.slogin_form),
    # sns로그인 (부분완료)
    ### http://127.0.0.1:8000/sns_login_form
    path('sns_login_form/account/', include('allauth.urls')),
    # path('logout', LogoutApi.as_view(), name="logout"),
    # path('login/', include(login_patterns)),

    # 로그인 페이지 이동 (완료)
    ### http://127.0.0.1:8000/login_form
    path('login_form/', views.login_form),
    
    # 로그인 (완료)
    ### http://127.0.0.1:8000/login/
    path('login/', views.login, name="login"),
    
    # 로그아웃 (완료)
    ### http://127.0.0.1:8000/logout
    path('logout/', views.logout),

    # 아이디 찾기 페이지 이동 (완료)
    ### http://127.0.0.1:8000/search_id
    path('search_id/', views.search_id),
    
    # 아이디 찾기 (완료)
    ### http://127.0.0.1:8000/forgot_id/
    path('forgot_id/', views.forgot_id),
    
    # 비밀번호 찾기 페이지 이동
    ### http://127.0.0.1:8000/search_pwd/
    path('search_pwd/',
         views.UserPasswordResetView.as_view(),
         name="password_reset"),

    # 비밀번호 찾기 메일 발송
    ### http://127.0.0.1:8000/search_pwd_done
    path('search_pwd_done/',
         views.PasswordResetDoneView.as_view(), 
         name="password_reset_done"),
    
    # 비밀번호 찾기 메일로 연결된 비밀번호변경 페이지
    ### http://127.0.0.1:8000/reset/<uidb64>/<token>/
    path('reset/<uidb64>/<token>//',
         views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    
    # 마이페이지/닉네임 수정 (완료)
    ### http://127.0.0.1:8000/my_page/nickname
    path('my_page/nickname/', views.nickname),
    
    # 마이페이지/비밀번호 수정 (완료)
    ### http://127.0.0.1:8000/my_page/change_pwd
    path('my_page/change_pwd/', views.change_pwd),

    #  회원가입 페이지 이동
    ### http://127.0.0.1:8000/sign_up
    path('sign_up/', views.sign_up),

    #  회원가입 (완료)
    ### http://127.0.0.1:8000/Ssign_up
    path('Ssign_up/', views.Ssign_up),
    
    #  회원탈퇴 (완료)
    ### http://127.0.0.1:8000/delete
    path('delete/', views.delete),

    # 게시판 페이지 이동
    ### http://127.0.0.1:8000/board
    path('board/', views.board),
    
    ### http://127.0.0.1:8000/board_des
    path('board_des/', views.board_des),
    
    ### http://127.0.0.1:8000/article
    path('article/', views.article),

    # my_page 이동
    ### http://127.0.0.1:8000/my_page
    path('my_page/', views.my_page),

    # map 페이지 이동
    ### http://127.0.0.1:8000/map
    path('map/', views.map),

    # map_api 연결
    ### http://127.0.0.1:8000/map
    path('map_api/', views.map_api),
]

