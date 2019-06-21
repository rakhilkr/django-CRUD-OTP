from django.db import models
from datetime import datetime
# Create your models here.


class Testdb(models.Model):
    name = models.CharField(max_length=20, blank=True)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()

class log(models.Model):
    User = models.CharField(max_length=20, blank=False)
    Password = models.CharField(max_length=20, blank=False)
    Password2 = models.CharField(max_length=20, blank=False)
    Name = models.CharField(max_length=35, blank=False)
    Email = models.CharField(max_length=20)
    Phone = models.IntegerField()


class Test(models.Model):
    name = models.CharField(max_length=20)
    age=models.IntegerField






