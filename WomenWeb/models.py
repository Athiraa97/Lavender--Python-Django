from django.db import models

# Create your models here.
class Customerdetails(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirmpassword= models.CharField(max_length=100, null=True, blank=True)

class contactdetails(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class billing(models.Model):
    Fname = models.CharField(max_length=30,null=True,blank=True)
    Lname = models.CharField(max_length=30,null=True,blank=True)
    Uname = models.CharField(max_length=30,null=True,blank=True)
    Email = models.CharField(max_length=30,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)

class itemcart(models.Model):
    Product=models.CharField(max_length=100,null=True,blank=True)

    quantity=models.IntegerField(null=True,blank=True)
    totalprice=models.IntegerField(null=True,blank=True)

