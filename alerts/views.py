import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Alert
from .serializers import AlertSerializer

#getting data from external api
api_url = "https://api.coinlore.net/api/tickers/"

@api_view(['GET'])
def get_cyrptocurrency_names(request):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        cryto_names = set(entry["name"] for entry in data["data"])
        crypto_names_list = list(cryto_names)
        return Response({'Cryto_names': crypto_names_list}, status=status.HTTP_200_OK)
    else:
        return Response({"error : Data not obtained"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#CRUD on alerts
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