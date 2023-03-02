# import requests

# url = "https://api.nobitex.ir/v2/orderbook/BTCUSDT"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(type(response.status_code))
# print(response.status_code)

# print(response.json())
# print(type(response.json()))


from main.create_db import create

create()