from ast import Name
from calendar import c
from datetime import date
from unicodedata import name
from django.db import models

# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=122)
    email=models.CharField( max_length=254)
    phoneno=models.CharField(max_length=10)
    desc=models.TextField()
   
    def __str__(self):
        return self.name


class Product(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    Category = models.CharField(max_length=300,default="")
    SubCategory = models.CharField(max_length=300,default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='products/images/',default="")
    brand = models.CharField(max_length=50,default="Zara")  
    rating=models.IntegerField(default=5)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __str__(self):
        return self.product_name

