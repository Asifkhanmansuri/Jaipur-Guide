from django.db import models

# Create your models here.
class Cinema_Data(models.Model):
    Image= models.ImageField(upload_to='image')
    Name=models.CharField(max_length=50)
    Address=models.TextField(max_length=100)
    Rating=models.IntegerField()
    Location=models.CharField(max_length=1000)