from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    productName=models.CharField(max_length=255)


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fullName=models.CharField(max_length=255)
    profileImage=models.ImageField(upload_to='borderImages/')
    userType=models.CharField(max_length=255,default='Normal User')
    number=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
    # axmad


class BorderRegistration(models.Model):
    theUser=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    idCardNo=models.CharField(max_length=255)
    expireDate=models.DateTimeField(null=True,blank=True)
    userState=models.CharField(max_length=255)
    userAddress=models.CharField(max_length=555)
    enteringDate=models.DateTimeField()
    nationality=models.CharField(max_length=255)
    fingerPrintCD=models.CharField(max_length=10000,default='')
    registrationDate=models.DateTimeField(auto_now=True)
    remainTime=models.DateTimeField(null=True,blank=True)
    products=models.ManyToManyField(Product)   


# title
# description
# theuser
# datetime