from django.db import models

class User(models.Model): 
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=128)  
    email=models.EmailField(max_length=50)