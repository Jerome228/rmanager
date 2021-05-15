from django.db import models

# Create your models here.
class AppData(models.Model):
    name = models.CharField(max_length=255)
    trg = models.CharField(max_length=3)
    hservers = models.CharField(max_length=255)
    pservers = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)