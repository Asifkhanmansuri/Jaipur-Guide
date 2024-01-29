from django.db import models

# Create your models here.
class Historical_Data(models.Model):
    Image= models.ImageField(upload_to='image')
    Name=models.CharField(max_length=50)
    Address=models.TextField(max_length=100)
    Rating=models.IntegerField(max_length=10000000)
    Location=models.CharField(max_length=1000)
    
    
class Place_Detail(models.Model):
    Image=models.ImageField(upload_to='image' , null=True, blank=True)
    Place_Name=models.CharField(max_length=50 ,null=True, blank=True)
    Wikipedia=models.TextField(max_length=100000000 ,null=True, blank=True)
    Wikipedia_Link=models.TextField(max_length=500, null=True, blank=True)
    Section_Name=models.CharField(max_length=50, null=True, blank=True)
   
    H_id=models.ForeignKey(Historical_Data, on_delete=models.DO_NOTHING, null=True)
    
class Place_Image(models.Model):
    Section_Image=models.ImageField(upload_to='image' ,null=True, blank=True)
    PlaceId= models.ForeignKey(Place_Detail, on_delete=models.DO_NOTHING, null=True )