from .models import TemperatureIn, TemperatureOut, TemperatureReturn
from rest_framework import serializers

class TemperatureInSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemperatureIn
        fields = ['date', 'current_temperature']


class TemperatureOutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemperatureOut
        fields = ['date', 'current_temperature']


class TemperatureReturnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemperatureReturn
        fields = ['date', 'current_temperature']