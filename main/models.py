from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

class Employee(models.Model):
    nameEmployee = models.CharField(max_length=255)
    age = models.IntegerField()
    hobby = models.TextField()    