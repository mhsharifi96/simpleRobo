import requests
import json



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
        url  =self.full_address +f'/trade/{update_id}/'
        data = {key:value}
        payload = json.dumps(data)
        response = requests.request("PATCH", url, headers=self.headers, data=payload)
        print(response.status_code)
        # print(response.text)
