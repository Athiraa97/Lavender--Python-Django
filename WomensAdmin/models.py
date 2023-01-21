from django.db import models

# Create your models here.
class employeedb(models.Model):
    Name = models.CharField(max_length=30,null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Image = models.ImageField(upload_to="profile",null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    CPassword = models.CharField(max_length=100,null=True,blank=True)

class categorydb(models.Model):
    CName = models.CharField(max_length=50,null=True,blank=True)
    CImage = models.ImageField(upload_to="profile", null=True, blank=True)
    Description = models.CharField(max_length=100,null=True,blank=True)

class productdb(models.Model):
    Product = models.CharField(max_length=50,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    PDescription = models.CharField(max_length=100,null=True,blank=True)
    PImage = models.ImageField(upload_to="profile",null=True,blank=True)
    Category = models.CharField(max_length=50,null=True,blank=True)
