from django.db import models

class Retreat(models.Model):
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=100)
    spots = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

