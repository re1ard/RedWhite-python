# -*- coding: utf-8 -*-

class RedWhiteError(Exception):
        def __init__(self,error):
                for key,value in error.items():
                        setattr(self,key,value)

        def __str__(self):
                return self.text

class RedWhiteUnknownCity(Exception):
        pass

class RedWhiteShop(Exception):
        pass

class RedWhiteUnknownShop(Exception):
        pass