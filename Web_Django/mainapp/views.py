from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "mainapp/index.html", {})

def Create_Posts_page(request):
    return render(request, "mainapp/Create_Posts_page.html", {})