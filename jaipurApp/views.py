from django.shortcuts import render, redirect
from .models import Historical_Home,Mall_Home, Cinema_Hall_Home, Market_Home, \
    Education_Home, Hotel_Home, Hospital_Home, Govt_Office_Home


# Create your views here.
def home(request):
    return render(request, 'home.html')

def home_page(request):
    historical= Historical_Home.objects.all()
    mall= Mall_Home.objects.all()
    cinema= Cinema_Hall_Home.objects.all()
    market= Market_Home.objects.all()
    education= Education_Home.objects.all()
    hotel= Hotel_Home.objects.all()
    hospital= Hospital_Home.objects.all()
    govt=Govt_Office_Home.objects.all()
    return render(request,'home.html', {"historical":historical, "mall":mall, "cinema":cinema, "market":market, "education":education, "hotel":hotel, "hospital":hospital, "govt":govt})
    
# creating the class for historical
# creating the class for login page
# def login(request):
#     return render(request, 'login.html')