from unicodedata import name
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    rechargeHistory = models.CharField(max_length=100000)
    
