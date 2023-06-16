from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainapp.car.car_view import Car_View
from django.utils import timezone
from django.contrib import messages
import cv2
import numpy as np
import base64
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from .models import User, Category, Community, Comment
from django.contrib.auth import get_user_model
# from .forms import SignupForm

# Create your views here.

# 메인페이지
def index(request):
    return render(request, "mainapp/index.html", {})

# 게시글 작성 페이지
def Create_Posts_page(request):
    return render(request, "mainapp/Create_Posts_page.html", {})

def car_repair_calculation_Page(request):
    return render(request, "mainapp/car_repair_calculation_Page.html", {})

# 이건 삭제예정(예전로그인폼)
def login_form1(request) :
    return render(request,
                  "mainapp/login/login_form1.html",
                  {})

# sns로그인 폼
def slogin_form(request) :
    return render(request,
                  "mainapp/login/sns_loginform.html",
                  {})

# 로그인 폼
def login_form(request) :
    return render(request,
                  "mainapp/login/loginform.html",
                  {})
    
# 로그인 성공
def login(request) :
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # 먼저 request 인자를 받아야함
        if form.is_valid():
            auth_login(request, form.get_user(), backend='django.contrib.auth.backends.ModelBackend')
            return render(request, "mainapp/index.html", {})
    else:
        form = AuthenticationForm()
        
    context = {
        'form' : form,
    }    
    return render(request, "mainapp/login/loginform.html", context)

#  로그아웃
def logout(request) : 
    auth_logout(request)
    return render(request, "mainapp/index.html", {})

#  아이디 찾기 페이지이동
def search_id(request) :
    return render(request,
                  "mainapp/login/id_search.html",
                  {})
    
#  아이디 찾기
def forgot_id(request) :
    if request.method == 'POST':
        email = request.POST.get('email')
        user_view = User.objects.get(email=email)
        username = user_view.username
    return render(request,
                  "mainapp/login/forgot_id.html",
                  {"username" : username})

# 비밀번호 찾기
def search_pwd(request) :
    return render(request,
                  "mainapp/login/pwd_search.html",
                  {})

# 닉네임 수정
def nickname(request) :
    if request.method == "POST" :
        form = CustomUserChangeForm(request.POST, instance=request.user)
        user = request.user
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, '성공적으로 닉네임을 변경하였습니다.')
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request,
                  "mainapp/my_Page.html",
                  {})
    else :
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request,
                  "mainapp/my_Page.html",
                  context)

#  비밀번호 변경
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
def change_pwd(request) :
    context= {}
    if request.method == 'POST':
        password = request.POST.get('password')
        user = request.user
        if check_password(password,user.password):
            new_password1 = request.POST.get("new_password1")
            new_password2 = request.POST.get("new_password2")
            if new_password1 == new_password2 :
                user.set_password(new_password1)
                user.save()
                auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
                messages.add_message(request, messages.INFO, '성공적으로 비밀번호를 변경하였습니다.')
                return render(request,
                    "mainapp/my_Page.html",
                    {})
            else :
                context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
        else:
    	    context.update({'error':"현재 비밀번호가 일치하지 않습니다."})
    return render(request,
                  "mainapp/my_Page.html",
                  context)
    
# 회원가입
def sign_up(request) :
    return render(request,
                  "mainapp/login/sign_up.html",
                  {})

# 회원가입 성공
def Ssign_up(request) :
    if request.method == "POST" :
        form = CustomUserCreationForm(request.POST)
        if form.is_valid() :
            form.save()

            return redirect('/login_form/')
        # else :
        #     print(form.is_valid())
        #     print(form)
        #     return redirect('')
    else : 
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, "mainapp/login/sign_up.html", context)
    msg = """
        <script type="text/javascript">
            alert('잘못된 접근입니다.');
            location.href = "/sign_up/";
        </script>
    """
    return HttpResponse(msg)
#    return render(request, "mainapp/login/sign_up.html", context)

#  회원탈퇴
def delete(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            username = request.user.username
            User.objects.filter(username=username).delete()
        auth_logout(request) 
    
        # session 지우기. 단 탈퇴후 로그아웃순으로 처리. 먼저 로그아웃하면 해당 request 객체 정보가 없어져서 삭제가 안됨.
        return render(request, "mainapp/index.html", {})
    else :
        return render(request,
                  "mainapp/my_Page.html",
                  {})

# 게시판
def board(request) :
    return render(request,
                  "mainapp/board.html",
                  {})

# 게시판 상세 보기
def board_des(request) :
    return render(request,
                  "mainapp/board_des.html",
                  {})

# 게시물 작성
def article(request) :
    return render(request,
                  "mainapp/article.html",
                  {})

# MY_PAGE
def my_page(request) :
    return render(request,
                  "mainapp/my_Page.html",
                  {})
    

# MAP
def map(request) :
    return render(request,
                  "mainapp/map.html",
                  {})

# MAP
def map_api(request) :
    return render(request,
                  "mainapp/map_api.html",
                  {})

import json
def car_repair_price(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        img_data = image_file.read()
        img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
        car_view = Car_View(img)
        car_data = car_view.result()

        # 넘파이 배열을 리스트로 변환
        car_data = car_data.astype(int)

        car_data_json = json.dumps(car_data.tolist())

        return HttpResponse(car_data_json, content_type='application/json')
    else:
        return HttpResponse("Image not found")
