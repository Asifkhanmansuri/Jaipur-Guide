from django.shortcuts import render
from .models import Cinema_Data

# Create your views here.
def cimena(request):
    cinema=Cinema_Data.objects.all()
    return render(request,"cinemaHall/cinema.html",{"cinema":cinema})