#from django.shortcuts import render

# Create your views here.
from .models import TemperatureIn, TemperatureOut, TemperatureReturn
from rest_framework import viewsets
from .serializer import TemperatureInSerializer
from .serializer import TemperatureOutSerializer
from .serializer import TemperatureReturnSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class TemperatureInViewSet(viewsets.ModelViewSet):
    queryset = TemperatureIn.objects.all()
    serialaizer_class = TemperatureInSerializer


@api_view(['GET', 'POST'])
def temperature_in_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temperature_in = TemperatureIn.objects.all()
        serializer = TemperatureInSerializer(temperature_in, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TemperatureInSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def temperature_out_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temperature_out = TemperatureOut.objects.all()
        serializer = TemperatureOutSerializer(temperature_out, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TemperatureOutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def temperature_return_list(request):
    if request.method == 'GET':
        temperature_return = TemperatureReturn.objects.all()
        serializer = TemperatureReturnSerializer(temperature_return, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TemperatureReturnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)