import requests
import json
from datetime import datetime
from time import sleep

from trade_api import RoboTradeApi

class HttpResponse:
    SUCCESS_CODE = 200

class SimpleRobo:

    def __init__(self) -> None:
        self.base_url = "https://api.nobitex.ir/v2/"
        self.slugs = {
            'order': "orderbook/",
            'trads': "trades/"
        }
        self.allow_coins = ["BTC", "ETH", "LTC","XRP","BCH"]
        self.main_coin = "USDT"
        self.responses = {}
        self._api = RoboTradeApi()
        self.tershold_0 =0.005
        self.tershold_1 =0.01
        self.tershold_2 =0.02
        self.tershold_3 =0.03
        self.SLEEP_TIME = 3



    def send_request(self,url):
        headers = {
            "content-type": "application/json"
        }
        response = requests.request("GET", url, headers=headers)
        if response.status_code == HttpResponse.SUCCESS_CODE:
            return response.json()
        return {}

    def request_order(self,coin):
        
        url= f"{self.base_url}{self.slugs['order']}{coin+self.main_coin}"
        response = self.send_request(url)
        if  response :
            return {
                'last_trade_price': response['lastTradePrice'],
                'first_bids': response['bids'][0][0],
                'first_asks': response['asks'][0][0],
                'server_titme': response['lastUpdate'],
                'create_time':str(datetime.now()),

            }
        return response
    
    def calc_profit(self,old_orders,new_order):
        response = {}
        for old_order in old_orders:
            last_trade_price_profit = \
                (float(new_order['last_trade_price'])-float(old_order['last_trade_price']))/float(new_order['last_trade_price'])
            # response['first_bids_profit'] = \
            #     (new_order['first_bids']-old_order['first_bids'])/new_order['first_bids']
            # response['first_asks_profit'] = \
            #     (new_order['first_asks']-old_order['first_asks'])/new_order['first_asks']
            trade_id = old_order['id']
            if last_trade_price_profit >= self.tershold_3 :

                response[trade_id] = self.tershold_3
            elif last_trade_price_profit >= self.tershold_2 :
                response[trade_id] = self.tershold_2
            elif last_trade_price_profit >= self.tershold_1 :
                response[trade_id] = self.tershold_1
            elif last_trade_price_profit >= self.tershold_0:
                response[trade_id] = self.tershold_0
            else :
                response[trade_id] = last_trade_price_profit
        print(response)
        return response

    
    def buy(self,coin):
        if coin in self.allow_coins:
            response=self.request_order(coin=coin)
            response['coin'] = coin.upper()
            response['market'] = coin
            response['sell'] = None
            self._api.insert(response)
        else:
            print(f"{coin} not allowed")
    
    def choice_sell(self,calc_profit_responses,new_order):
        for id,profit in calc_profit_responses.items():
            if profit > self.tershold_1:
                self._api.update(update_id=id, key='status',value='close')
                self._api.update(update_id=id,key='report',value=json.dumps(new_order))
                #TODO : send_email , add order for sell
            else:
                print("Unfortunately, the market is at a loss")
    
    def sell(self,coin):
        # if market in self.allow_coins:
        old_orders = self._api.get_all(coin=coin) 
        new_order = self.request_order(coin=coin)
        calc_profit_responses = self.calc_profit(old_orders=old_orders,new_order=new_order)
        self.choice_sell(calc_profit_responses,new_order = new_order)
            
                

    def seller(self):
        while True : 
            for coin in self.allow_coins:
                if self._api.count_trade(coin=coin) > 0:
                    self.sell(coin=coin)
            sleep(self.SLEEP_TIME)
            print('run')

    
