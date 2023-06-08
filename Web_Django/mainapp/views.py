from django.shortcuts import render

from .models import User, User_img, User_service, Provision, Provision_history, Naver_account, google_account, Kakao_account, Category, Community, Comment 

# Create your views here.
def index(request):
    return render(request, "mainapp/index.html", {})

def Create_Posts_page(request):
    return render(request, "mainapp/Create_Posts_page.html", {})