from django.db import models

# Create your models here.


class TemperatureIn(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    current_temperature = models.FloatField(null=True, blank=True)


class TemperatureOut(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    current_temperature = models.FloatField(null=True, blank=True)


class TemperatureReturn(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    current_temperature = models.FloatField(null=True, blank=True)