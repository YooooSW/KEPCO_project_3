from django.shortcuts import render
from django.http import HttpResponse
from mainapp.car.car_view import Car_View
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

def test(request):
    return render(request, "mainapp/test.html", {})


def car_repair_calculation(request):
    
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES.get('image')
        image_data = request.FILES['image']
        img_data = image_file.read()


        # image_data = base64.b64encode(img_data).decode('utf-8')
        # img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
        img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
        image_url = f"/media/{image_file.name}"  # Update this based on your image's actual path or URL
    else:
        image_url = None
        image_data = None
    car_view = Car_View(img)
    car_data = car_view.result()
    return render(request, 'mainapp/car_repair_calculation_Page.html', {'car_data': car_data, 'image_data': image_data})

def car_repair_price(request):
    
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES.get('image')
        image_data = request.FILES['image']
        img_data = image_file.read()
    return HttpResponse(image_data)

    #     img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)
    #     image_url = f"/media/{image_file.name}"  # Update this based on your image's actual path or URL
    # else:
    #     image_url = None
    #     image_data = None
    # car_view = Car_View(img)
    # car_data = car_view.result()
    # return render(request, 'mainapp/car_repair_calculation_Page.html', {'car_data': car_data, 'image_data': image_data})
