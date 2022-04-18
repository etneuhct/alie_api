from django.db import models

# Create your models here.
from django.utils.timezone import now


class BotIdentity(models.Model):
    key = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=now)
    voice = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)