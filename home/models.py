from ast import Name
from calendar import c
from datetime import date
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

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
    id=models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    Category = models.CharField(max_length=300,default="")
    SubCategory = models.CharField(max_length=300,default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='products/images/',default="")
    brand = models.CharField(max_length=50,default="Zara")  
    rating=models.IntegerField(default=5)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default="Male")
    def __str__(self):
        return self.product_name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size=models.CharField(max_length=3,default="s")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    name=   models.CharField(max_length=100,default='')
    email = models.EmailField(max_length=100, default='default@example.com')

    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    total=models.IntegerField()
    

    def __str__(self):
        return f'{self.user.username} - {self.address_line_1}, {self.city}'