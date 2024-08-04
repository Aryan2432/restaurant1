from django.db import models

class one(models.Model):
    a1=models.CharField(max_length=20)
    a2=models.CharField(max_length=20)
    a3=models.CharField(max_length=20)
    a4=models.DateField()
    a5=models.TimeField()
    a6=models.CharField(max_length=300)
# Create your models here.
