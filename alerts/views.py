import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Alert
from .serializers import AlertSerializer, CryptoDataSerializer




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

@api_view(['GET'])
def get_crypto_data(request, name):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        crypto_data = None
        for entry in data["data"]:
            if entry["name"] == name:
                crypto_data = {
                    "Name" : entry["name"],
                    "Price_USD" : entry["price_usd"],
                    "Change_percentage" : entry["percent_change_24h"]
                }
                break
        if crypto_data:
            serializer = CryptoDataSerializer(data = crypto_data)
            if serializer.is_valid():
                return Response(serializer.validated_data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "No such Cryptocurrency"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"Error": "Failed to fetch data from api"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




#CRUD on alerts
@api_view(['GET'])
def get_all_alerts(request):
    alerts = Alert.objects.filter(user=request.user)
    serialiazer = AlertSerializer(alerts, many=True)
    return Response(serialiazer.data)

@api_view(['GET'])
def get_alert(request, pk):
    alert = Alert.objects.get(id=pk)
    serializer = AlertSerializer(alert)
    return Response(serializer.data)

@api_view(['POST'])
def create_alert(request):
    request.data['user'] = request.user.id
    serialiazer = AlertSerializer(data=request.data)
    if serialiazer.is_valid():
        serialiazer.save()
        return Response(serialiazer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_alert(request,pk):
    try:
        alert = Alert.objects.get(id=pk, user=request.user)
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



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Alert

def your_model_list(request):
    object_list = Alert.objects.all()
    
    paginator = Paginator(object_list, 10)

    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return render(request, 'your_model_list.html', {'objects': objects})
