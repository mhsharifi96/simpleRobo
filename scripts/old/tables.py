from peewee import *
import datetime
db = SqliteDatabase('robo.db')

class BaseModel(Model):
    class Meta:
        database = db


class ConfigTrade(BaseModel):
    coin = CharField(max_length=6)
    max_open_order = IntegerField(default=5)
    threshold_profit = FloatField(default=0.02)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

class Trade(BaseModel):
    STATUS_CHOICES = (
        ('open','open'),
        ('close','close'),
    )
    coin = CharField(max_length=6)
    price = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField()
    status = CharField(max_length=6,choices=STATUS_CHOICES)
    report = TextField(null=True)

 