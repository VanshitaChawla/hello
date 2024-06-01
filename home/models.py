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
    