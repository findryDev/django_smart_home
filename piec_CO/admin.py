from django.contrib import admin
from .models import TemperatureIn, TemperatureOut, TemperatureReturn

# Register your models here.
admin.site.register(TemperatureIn)
admin.site.register(TemperatureOut)
admin.site.register(TemperatureReturn)