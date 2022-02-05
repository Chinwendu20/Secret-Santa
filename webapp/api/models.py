from django.db import models

# Create your models here.

class People(models.Model):
	Name=models.CharField(max_length=20)
	Email=models.EmailField()
