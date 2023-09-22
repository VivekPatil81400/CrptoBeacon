from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Alert
from .serializers import AlertSerializer

# Create your views here.
@api_view(['GET'])
def get_all_alerts(request):
    alerts = Alert.objects.all()
    serialiazer = AlertSerializer(alerts, many=True)
    return Response(serialiazer.data)

@api_view(['GET'])
def get_alert(request, pk):
    alert = Alert.objects.get(id=pk)
    serializer = AlertSerializer(alert)
    return Response(serializer.data)

@api_view(['POST'])
def create_alert(request):
    serialiazer = AlertSerializer(data=request.data)
    if serialiazer.is_valid():
        serialiazer.save()
        return Response(serialiazer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_alert(request,pk):
    try:
        alert = Alert.objects.get(id=pk)
    except Alert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serialiazer = AlertSerializer(alert, data=request.data)
    if serialiazer.is_valid():
        serialiazer.save()
        return Response(serialiazer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_alert(request, pk):
    alert = Alert.objects.get(id=pk)
    alert.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)