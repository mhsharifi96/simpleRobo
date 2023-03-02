from rest_framework import serializers
from .models import Trade,ConfigTrade

class TradeSerializers(serializers.ModelSerializer):

    class Meta: 
        fields = "__all__"
        model = Trade

class ConfigTradeSerializers(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = ConfigTrade