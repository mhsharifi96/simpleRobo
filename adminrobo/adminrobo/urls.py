from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from main.views import ConfigTradeViewSet,TradeViewSet

router = DefaultRouter()
router.register(r'trade/config', ConfigTradeViewSet, basename='config')
router.register(r'trade', TradeViewSet, basename='trade')

# custom link
coin_trade = TradeViewSet.as_view({'get': 'trade'})
count_coin_trade = TradeViewSet.as_view({'get': 'count_trade'})


urlpatterns = router.urls
urlpatterns += [
    path('admin/', admin.site.urls),
    path('trade/<str:coin>/<str:status>',coin_trade,name='coin_trade'),
    path('trade/<str:coin>/<str:status>/count',count_coin_trade,name='count_coin_trade')

]

