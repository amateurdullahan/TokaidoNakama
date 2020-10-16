#!/usr/bin/python3
"""player objects"""

class Player():
        def __init__(self, color="", score=0, coins=7, board_space=0, pano_paddy=0, pano_mt=0, pano_sea=0):
            """initializing the players"""
            self.color = color
            self.score = score
            self.coins = coins
            self.board_space = board_space
            self.pano_paddy = pano_paddy
            self.pano_mt = pano_mt
            self.pano_sea = pano_sea

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
        def board_space(self):
            """comment"""
            return self.__board_space

        @board_space.setter
        def board_space(self, value):
            """comment"""
            self.__board_space = value

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


class Achievements():
        def __init__(self, pano_paddy_bonus=0, pano_mt_bonus=0, pano_sea_bonus=0):
            """initializing the players"""
            self.pano_paddy_bonus = pano_paddy_bonus
            self.pano_mt_bonus = pano_mt_bonus
            self.pano_sea_bonus = pano_sea_bonus

        @property
        def pano_paddy_bonus=0(self):
            """comment"""
            return self.__pano_paddy_bonus=0

        @color.setter
        def pano_paddy_bonus=0(self, value):
            """comment"""
            self.__pano_paddy_bonus=0 = value
