from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action


from .models import ConfigTrade, Trade
from .serializers import ConfigTradeSerializers, TradeSerializers

class ConfigTradeViewSet(viewsets.ModelViewSet):
    serializer_class = ConfigTradeSerializers
    queryset = ConfigTrade.objects.all()
    

class TradeViewSet(viewsets.ModelViewSet):

    serializer_class = TradeSerializers
    queryset = Trade.objects.all()

    @action(detail=True, methods=['get'])
    def trade(self, request, coin:str=None,status:str='open'):
        coin = coin.upper()
        open_trades = Trade.objects.filter(coin=coin, status=status)
        serializers = self.get_serializer(open_trades, many=True)
        return Response(serializers.data)
    
    @action(detail=True,methods=['get'])
    def count_trade(self,request,coin:str, status:str='open'):
        coin = coin.upper()
        trades_count = Trade.objects.filter(coin=coin, status=status).count()
        return Response({
            'status':status,
            'count':trades_count
        })

