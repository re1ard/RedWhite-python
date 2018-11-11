# -*- coding: utf-8 -*-
"""
                City Item
		"cityId": 4990,
		"name": "\u0410\u0431\u0434\u0443\u043b\u0438\u043d\u043e",
		"regionId": 797,
		"latitude": "53.6819539",
		"longitude": "53.6474802"
"""
class City:
        def __init__(self,data):
                for key,value in data.items():
                        setattr(self,key,value)

        def __str__(self):
                return self.name

        def __int__(self):
                return self.cityId

"""
                Product Item
		"productId": 8752, //индификатор
		"name": "\u042f\u0439\u0446\u043e \u043a\u0443\u0440\u0438\u043d\u043e\u0435 \u04211 \u0413\u041e\u0421\u0422", //название
		"originName": "\u042f\u0439\u0446\u043e \u043a\u0443\u0440\u0438\u043d\u043e\u0435", //оригинальное название
		"description": "" // описание
		"price": 5.2800000000000002, //цена
		"measure": "1 \u0448\u0442", //ед.измерения
		"img": "http:\/\/retail-kb.itnap.ru\/i\/f718bec83f1adef8a588f56186381555\/1000x1000\/42\/a9\/42a9e438253ed2c7c540c3d36441cb73.jpg", //каринка
		"labelImg": "",
		"backLabelImg": "http:\/\/retail-kb.itnap.ru\/i\/911a3d1f101d2add2797b09c5eef0203\/1000x1000\/f7\/54\/f7542dd862ae47861a63bc0a1c120312.jpg",
		"countryFlag": "http:\/\/retail-kb.itnap.ru\/i\/02a2df2ceb2f9a7832727c0464fd7d90\/1000x1000\/94\/bd\/94bd280cfc31bec2790960603af1c2d6.jpg",
		"degree": 0,
		"temperature": 0,
		"flavor": null,
		"manufacturerName": null,
		"manufacturerImg": "",
		"latitude": null,
		"longitude": null,
		"percent": 0,
		"countForSale": null,
		"isHit": false,
		"isSale": false,
		"isSpecial": false,
		"quantityAll": 5882770,
		"countShops": 6974,
		"turnDays": 4,
		"dateUpdated": {
			"date": "2018-11-11 00:00:00.000000",
			"timezone_type": 3,
			"timezone": "Europe\/Moscow"
		},
		"dateCreated": {
			"date": "2017-07-04 06:30:01.304094",
			"timezone_type": 3,
			"timezone": "Europe\/Moscow"
		},
		"shopId": 1240,
		"isNew": false,
		"isRemains": false,
		"priority": 0,
		"invisible": false,
		"subProduct": false,
		"hiddenPriceMiddle": false,
		"hiddenPriceSpecial": false,
		"hiddenQuantity": false,
		"quantity": 870, //количество в выбраном магазине
		"country": [{
			"id": 2,
			"name": "\u0420\u043e\u0441\u0441\u0438\u044f"
		}],
		"wine_ratings_short": null,
		"rating": {
			"productId": 8752,
			"voteCount": 940,
			"voteSum": 3299,
			"rating": 4,
			"average": 4
		}
"""
class Product:
        def __init__(self,data):
                for key,value in data.items():
                        setattr(self,key,value)

        def __str__(self):
                return self.name.encode("utf8")

        def __unicode__(self):
                return self.name

        def __int__(self):
                return self.productId

        def __float__(self):
                return self.price


"""
                        Shop Item
			"shop_id": 1240,
			"name": "\u043f\u0440-\u0442. \u041b\u0435\u043d\u0438\u043d\u0430, 57\/\u0443\u043b. \u041b\u044c\u0432\u0430 \u0422\u043e\u043b\u0441\u0442\u043e\u0433\u043e, 114\u0431",
			"latitude": "54.183402",
			"longitude": "37.60823",
			"is_plus": true,
			"is_beer": true,
			"city_id": 1450,
			"no_alcohol": false,
			"phone": "79307903116",
			"alc_time_start_weekdays": "14:00",
			"alc_time_end_weekdays": "22:00",
			"alc_time_start_weekend": "12:00",
			"alc_time_end_weekend": "22:00",
			"alc_time_start_sunday": null,
			"alc_time_end_sunday": null,
			"location": "0101000020E610000019390B7BDACD4240B0027CB779174B40",
			"schedule": "09:00-22:05",
			"stations": []
"""
class Shop:
        def __init__(self,data):
                for key,value in data.items():
                        setattr(self,key,value)

        def __str__(self):
                return self.name

        def __int__(self):
                return self.shop_id

"""
			Catalog Item
			"categoryId": 10100,
			"parentId": 0,
			"name": "\u041d\u043e\u0432\u0438\u043d\u043a\u0438",
			"priority": -3,
			"hiddenPriceMiddle": null,
			"hiddenPriceSpecial": null,
			"hiddenQuantity": null
"""

class Catalog:
	def __init__(self,data):
		for key,value in data.items():
                        setattr(self,key,value)

	def __str__(self):
                return self.name

        def __int__(self):
                return self.categoryId		