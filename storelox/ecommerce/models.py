from django.db import models

# Create your models here.

# User Model
class User(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=20)
    phone_Number = models.CharField(max_length=11)
    email = models.EmailField(max_length=120)




    
    