from django.db import models

# Create your models here.
class Historical_Home(models.Model):
    image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100, default=0)
class Hospital_Home(models.Model):
    image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100, default=0)
class Hotel_Home(models.Model):
    image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100, default=0)
class Govt_Office_Home(models.Model):
    image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100, default=0)
class Education_Home(models.Model):
    image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100, default=0)
class Market_Home(models.Model):
    image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100, default=0)
class Mall_Home(models.Model):
    image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100, default=0)
class Cinema_Hall_Home(models.Model):
    image=models.ImageField(upload_to='image')
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100, default=0)
