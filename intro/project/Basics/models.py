from django.db import models

# Create your models here.
class StudentDetailsModel(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    