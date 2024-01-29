from django.shortcuts import render
from .models import Hospital_Data

# Create your views here.
def hospital(request):
    Hospital= Hospital_Data.objects.all()
    return render(request, "hospital/hospital.html", {"hospital":Hospital})