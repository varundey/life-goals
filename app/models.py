from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Event(models.Model):
    title = models.CharField(max_length=20)
    description= models.CharField(max_length=200, blank=True)
    end_date = models.DateField(default=date.today)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['done', 'end_date']

    def save(self, *args, **kwargs):
        if self.end_date < date.today():
            raise ValidationError("End date has already passed!")
        super(Event, self).save(*args, **kwargs)
