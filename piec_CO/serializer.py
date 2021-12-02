from .models import TemperatureIn, TemperatureOut, TemperatureReturn
from rest_framework import serializers

class TemperatureInSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemperatureIn
        fields = ['pub_date', 'current_temperature']


class TemperatureOutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemperatureOut
        fields = ['pub_date', 'current_temperature']


class TemperatureReturnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemperatureReturn
        fields = ['pub_date', 'current_temperature']