from django.shortcuts import render
from .models import Historical_Data, Place_Detail, Place_Image

# Create your views here.
def historical(request):
    historical_data=Historical_Data.objects.all()
    return render (request,'historical.html',{"historical_data":historical_data})

def place_details(request, pk):
    if request.method=='GET':
        details=Place_Detail.objects.get(H_id=pk)
        placeImage=Place_Image.objects.filter(PlaceId=pk)
        
    return render(request, 'historical/city_palace.html', {"viewmore":details, 'placeImage':placeImage})
    
        
        
        