from django.db import models
class Thing(models.Model):
    name = models.CharField(
    max_length=30,
    unique=True,
    blank=False,
    )
    description = models.CharField(
    unique=False,
    max_length=120,
    )
    quantity = models.IntegerField(
    
    )
# Create your models here.
