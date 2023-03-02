from django.contrib import admin
from .models import Trade,ConfigTrade
# Register your models here.

admin.site.register(ConfigTrade)

class TradeAdmin(admin.ModelAdmin):
    list_filter = ['coin','status']
    list_display = ['id','coin','status','last_trade_price','first_asks',
                    'first_bids','created_at','updated_at']
    
admin.site.register(Trade,TradeAdmin)