from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Retreat(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    spots = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=50)
