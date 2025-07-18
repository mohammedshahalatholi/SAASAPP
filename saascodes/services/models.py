from django.db import models

# Create your models here.
class Services(models.Model):
    Title=models.CharField(max_length=100)
    Link=models.CharField(max_length=100)
    Discription=models.CharField(max_length=100)