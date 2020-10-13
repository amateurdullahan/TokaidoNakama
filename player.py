#!/usr/bin/python3
"""player objects"""

class Player():
        def __init__(self, color="", score=0, coins=0, pano_paddy=0, pano_mt=0, pano_sea=0):
            """initializing the players"""
            self.color = color
            self.score = score
            self.coins = coins
            self.panoramas = panoramas

        @property
        def color(self):
            """comment"""
            return self.__color

        @color.setter
        def color(self, string):
            """comment"""
            self.__color = string

        @property
        def score(self):
            """comment"""
            return self.__score

        @score.setter
        def score(self, value):
            """comment"""
            self.__score = value

        @property
        def coins(self):
            """comment"""
            return self.__coins

        @coins.setter
        def coins(self, value):
            """comment"""
            self.__coins = value

        @property
        def pano_paddy(self):
            """comment"""
            return self.__pano_paddy

        @pano_paddy.setter
        def pano_paddy(self, value):
            """comment"""
            self.__pano_paddy = value

        @property
        def pano_mt(self):
            """comment"""
            return self.__pano_mt

        @pano_mt.setter
        def pano_mt(self, value):
            """comment"""
            self.__pano_mt = value

        @property
        def pano_sea(self):
            """comment"""
            return self.__pano_sea

        @pano_sea.setter
        def pano_sea(self, value):
            """comment"""
            self.__pano_sea = value
