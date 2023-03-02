from django.db import models

# Create your models here.

class ConfigTrade(models.Model):
    coin = models.CharField(max_length=6)
    full_name = models.CharField(max_length=55)
    description = models.CharField(max_length=500,blank=True,null=True)
    max_open_order = models.IntegerField(default=5)
    threshold_profit = models.FloatField(default=0.02)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.coin

class Trade(models.Model):
    STATUS_CHOICES = (
        ('open','open'),
        ('close','close'),
        ('not_active','not_active')
    )
    coin = models.CharField(max_length=6)
    last_trade_price = models.FloatField()
    first_asks = models.FloatField(null=True)
    first_bids = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15,choices=STATUS_CHOICES)
    report = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return f"{str(self.id)} - {self.coin}"

