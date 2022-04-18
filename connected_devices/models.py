from django.db import models

# Create your models here.

class Mouth(models.Model):
    host = models.CharField(max_length=255)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    exe = models.CharField(max_length=100)
    room = models.CharField(max_length=20)