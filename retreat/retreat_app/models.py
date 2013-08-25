from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Retreat(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    spots = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=50)

class Attendee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    retreat = models.ForeignKey(Retreat)