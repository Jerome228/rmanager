from django.db import models


# Create your models here.
class AppData(models.Model):
    name = models.CharField(max_length=255)
    trg = models.CharField(max_length=3)
    hservers = models.CharField(max_length=255)
    pservers = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Application Data for {self.trg}'
    
    def __repr__(self):
        return f'<AppData of {self.trg} ({self.pk})>'
