from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model
class Thing(Model):
    name = models.CharField(
    max_length=30,
    unique=True,
    blank=False,
    )
    description = models.CharField(
    unique=False,
    max_length=120,
    blank=True
    )
    quantity = models.IntegerField(
    validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
# Create your models here.
