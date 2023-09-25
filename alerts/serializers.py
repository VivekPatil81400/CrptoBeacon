from .models import Alert
from rest_framework import serializers

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'

class CryptoDataSerializer(serializers.Serializer):
    Name = serializers.CharField()
    Price_USD = serializers.DecimalField(max_digits=10, decimal_places=8)
    Change_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)