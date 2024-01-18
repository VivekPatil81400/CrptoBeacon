from celery import shared_task
import time
import requests
from .serializers import CryptoDataSerializer 
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def fetch_bitcoin_price():
    try:
        response = requests.get('http://127.0.0.1:8000/get_crypto_data/Bitcoin')
        response.raise_for_status()
        bitcoin_data = response.json()

        serializer = CryptoDataSerializer(data=bitcoin_data)
        if serializer.is_valid():
            serializer.save()
            logger.info('Bitcoin price fetched successfully.')
        else:
            logger.error('Failed to serialize Bitcoin data: %s', serializer.errors)

    except requests.RequestException as e:
        logger.error('Failed to fetch Bitcoin price: %s', str(e))
