# -*- coding: utf-8 -*-
import requests

from kbroutes import *
from kbtypes import *
from kberrors import *

class RedWhite:
        cities = {}
        shops = {}
        current_city = None
        current_shop = None
        def __init__(self):
                self.http = requests.Session()
                self.http.headers = {"User-Agent":"RedWhite/2.9.1 (Innotek GmbH VirtualBox; Android 27; 2; 0509-de40-a32e-6eb2)"}
                self.http.verify = False

        def getCities(self):
                response = getattr(self.http,GET_CITIES[1].lower())(GET_CITIES[0]).json()
                if response['success']:
                        for city in response['result']:
                                self.cities.update({city['name']:City(city)})
                        return self.cities
                else:
                        raise RedWhiteError(response['error'])

        def setCity(self,name):
                if not self.cities:
                        self.getCities()
                if name in self.cities.keys():
                        self.current_city = self.cities[name]
                        return self.current_city
                raise RedWhiteUnknownCity()

        def getShops(self):
                if not self.current_city:
                        raise RedWhiteShop('Not setted city')
                response = getattr(self.http,SEARCH_CITY[1].lower())(SEARCH_CITY[0].format(self.current_city.cityId)).json()
                if response['success']:
                        for shop in response['result']['shops']:
                                self.shops.update({int(shop['shop_id']):Shop(shop)})
                        return self.shops
                else:
                        raise RedWhiteError(response['error'])

        def setShop(self,shopid):
                if not self.current_shop:
                        self.getShops()
                if int(shopid) in self.shops.keys():
                        self.current_shop = self.shops[int(shopid)]
                        return self.current_shop
                raise RedWhiteUnknownShop()

        def search(self,q):
                data = {"offset":0,"type":"full","limit":20,"query":q,"shop_id":int(self.current_shop)}
                response = getattr(self.http,SEARCH_PRODUCT[1].lower())(SEARCH_PRODUCT[0],data = data).json()
                if response["success"]:
                        for product in response['result']:
                                yield Product(product)
                else:
                        raise RedWhiteError(response['error'])