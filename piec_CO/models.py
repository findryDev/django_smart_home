from django.db import models

# Create your models here.


class TemperatureIn(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    current_temperature = models.FloatField(null=True, blank=True)


class TemperatureOut(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    current_temperature = models.FloatField(null=True, blank=True)


class TemperatureReturn(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    current_temperature = models.FloatField(null=True, blank=True)