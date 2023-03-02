import requests
import json
from datetime import datetime
from time import sleep
class HttpResponse:
    SUCCESS_CODE = 200


class RoboTradeApi:
    def __init__(self) -> None:
        self.address = "http://127.0.0.1"
        self.port = "8000"
        self.full_address = self.address +":"+ self.port
        self.headers = {
            "content-type": "application/json"
        }
        self.MAX_OPEN_TRADE =3
    def request(self,slug):
        url = self.full_address + "/"+slug
        response = requests.request("GET", url, headers=self.headers)
        return response
    def get(self,key):
        slug = 'trade/'
        if key:
            slug += key

        response = self.request(slug=slug)
        return response.json()
    
    def get_all(self,coin:str,status:str="open"):
        slug = 'trade/'+coin+'/'+status
        response = self.request(slug=slug)
        return response.json()
    
    def count_trade(self,coin:str,status:str='open'):
        slug = 'trade/'+coin+'/'+status+'/'+'count'
        response = self.request(slug=slug)
        if response:
            response = response.json()
            return response['count']
    
    
    def search(self,market):
        pass

    def insert(self,data):
        count_open_trade = self.count_trade(coin=data['coin'])
        if count_open_trade < self.MAX_OPEN_TRADE:
            data['status']='open'
        else :
            data['status'] = 'not_active'

        url  =self.full_address +'/trade/'
        payload = json.dumps(data)
        response = requests.request("POST", url, headers=self.headers, data=payload)
        print(response.text)
        

    def update(self,update_id,key,value):
        url  =self.full_address +f'/trade/{update_id}'
        data = {key:value}
        payload = json.dumps(data)
        response = requests.request("PATCH", url, headers=self.headers, data=payload)
        print(response.text)

    

class SampleRobo:

    def __init__(self) -> None:
        self.base_url = "https://api.nobitex.ir/v2/"
        self.slugs = {
            'order': "orderbook/",
            'trads': "trades/"
        }
        self.markets = ["BTC", "ETH", "LTC"]
        self.main_coin = "USDT"
        self.responses = {}

        self._api = RoboTradeApi()
        self.tershold_0 =0.005
        self.tershold_1 =0.01
        self.tershold_2 =0.02
        self.tershold_3 =0.03



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
        if coin in self.markets:
            response=self.request_order(coin=coin)
            response['coin'] = coin.upper()
            response['market'] = coin
            response['sell'] = None
            self._api.insert(response)
        else:
            print(f"{coin} not allowed")
    
    def choice_sell(self,calc_profit_responses):
        for id,profit in calc_profit_responses.items():
            if profit > self.tershold_1:
                self._api.update(update_id=id, key='status',value='close')
                #send_email
            else:
                print("Unfortunately, the market is at a loss")
    
    def sell(self,coin):
        # if market in self.markets:
        old_orders = self._api.get_all(coin=coin) 
        new_order = self.request_order(coin=coin)
        calc_profit_responses = self.calc_profit(old_orders=old_orders,new_order=new_order)
        self.choice_sell(calc_profit_responses)
            
                

    def seller(self):
        while True : 
            for coin in self.markets:
                if self._api.count_trade(coin=coin) > 0:
                    self.sell(coin=coin)
            sleep(3)
            print('run')

    




if __name__ == "__main__":
    robo = SampleRobo()
    # robo.buy("BTC")
    robo.seller()
