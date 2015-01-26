from django.db import models
from datetime import datetime


class TrafficReport(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=50)
    light = models.CharField(max_length=10)
    when = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.light
