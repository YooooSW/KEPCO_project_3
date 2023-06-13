from django.shortcuts import render
from django.http import HttpResponse
from mainapp.car.car_view import Car_View
from django.utils import timezone
import cv2
import numpy as np
import base64


from .models import User, User_img, User_service, Provision, Provision_history, Naver_account, google_account, Kakao_account, Category, Community, Comment 

# Create your views here.
def index(request):
    return render(request, "mainapp/index.html", {})

def Create_Posts_page(request):
    return render(request, "mainapp/Create_Posts_page.html", {})

def car_repair_calculation_Page(request):
    return render(request, "mainapp/car_repair_calculation_Page.html", {})

def login_form1(request) :
    return render(request,
                  "mainapp/login/login_form1.html",
                  {})

def slogin_form(request) :
    return render(request,
                  "mainapp/login/sns_loginform.html",
                  {})

def login_form(request) :
    return render(request,
                  "mainapp/login/loginform.html",
                  {})

def search_id(request) :
    return render(request,
                  "mainapp/login/id_search.html",
                  {})

def search_pwd(request) :
    return render(request,
                  "mainapp/login/pwd_search.html",
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
