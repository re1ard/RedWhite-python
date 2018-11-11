# -*- coding: utf-8 -*-

POST = u"POST"
GET = u"GET"

GATEWAY_API = u"https://retail-kb.itnap.ru/api/"

GET_UPDATED = (GATEWAY_API + u"getUpdated/",POST)
GET_CITIES = (GATEWAY_API + u"products/getCities/",POST)
GET_CATEGORIES = (GATEWAY_API + u"products/getCategories/",POST)

SEARCH_PRODUCT = (GATEWAY_API + u"products/search/",POST)
SEARCH_CITY = (GATEWAY_API + u"v1/shops/find_by_city/{}",GET)
