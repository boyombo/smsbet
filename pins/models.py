from django.db import models
from datetime import datetime


class Batch(models.Model):
    created_on = models.DateTimeField(editable=False, default=datetime.now)

    class Meta:
        verbose_name_plural = 'Batches'

    def __unicode__(self):
        return self.created_on.strftime('%Y-%m-%d')

    @property
    def used(self):
        return self.pin_set.filter(used=True).count()

    @property
    def count(self):
        return self.pin_set.count()

    def download_pins(self):
        return "<a href='/download/pins/?batch=%s'>download pins</a>" % self.pk
    download_pins.allow_tags = True


class Pin(models.Model):
    pin = models.CharField(max_length=16, unique=True)
    batch = models.ForeignKey(Batch)
    used = models.BooleanField(default=False)

    def __unicode__(self):
        return self.pin
