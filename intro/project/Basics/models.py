from django.db import models

# Create your models here.
class StudentDetailsModel(models.Model):
    name=models.CharField(max_length=100,null=True, blank=True)
    phone_number=models.CharField(max_length=15,null=True, blank=True)
    gender=models.CharField(max_length=10,null=True, blank=True)
    standard=models.IntegerField(null=True, blank=True)


"""
anish
sahil
kanhaya
riya

"""