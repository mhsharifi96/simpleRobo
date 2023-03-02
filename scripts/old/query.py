from main.tables import Trade,ConfigTrade


class BaseQuery():
    def get(self,key):
        pass
    def insert(self):
        pass

    def update(self):
        pass
    def delete(self):
        pass

class TradeQuery:
    def __init__(self) -> None:
        self.cls = Trade

    def get(self,value):
        
        response =self.cls.select().where(self.cls == value) 
        return response
            