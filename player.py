#!/usr/bin/python3
"""player objects"""
from deck import Deck

class Player():
        def __init__(self, color="", playerdeck=Deck(), score=0, coins=7, board_space=99, pano_paddy=0, pano_mt=0, pano_sea=0, sv_type_first="", sv_type_second="", sv_type_third="", sv_type_fourth="", bather_bonus=0, icon=0, donation=0, temple_bonus=0, chatterbox_bonus=0, collector_bonus=0, gourmet_bonus=0):
            """initializing the players"""
            self.playerdeck = playerdeck
            self.color = color
            self.score = score
            self.coins = coins
            self.board_space = board_space
            self.pano_paddy = pano_paddy
            self.pano_mt = pano_mt
            self.pano_sea = pano_sea
            self.sv_type_first = sv_type_first
            self.sv_type_second = sv_type_second
            self.sv_type_third = sv_type_third
            self.sv_type_fourth = sv_type_fourth
            self.bather_bonus = bather_bonus
            self.playerdeck = playerdeck
            self.icon = icon
            self.donation = donation
            self.temple_bonus = temple_bonus
            self.chatterbox_bonus = chatterbox_bonus
            self.collector_bonus = collector_bonus
            self.gourmet_bonus = gourmet_bonus

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

        @property
        def sv_type_first(self):
            """comment"""
            return self.__sv_type_first

        @sv_type_first.setter
        def sv_type_first(self, string):
            """comment"""
            self.__sv_type_first = string

        @property
        def sv_type_second(self):
            """comment"""
            return self.__sv_type_second

        @sv_type_second.setter
        def sv_type_second(self, string):
            """comment"""
            self.__sv_type_second = string

        @property
        def sv_type_third(self):
            """comment"""
            return self.__sv_type_third

        @sv_type_third.setter
        def sv_type_third(self, string):
            """comment"""
            self.__sv_type_third = string

        @property
        def sv_type_fourth(self):
            """comment"""
            return self.__sv_type_fourth

        @sv_type_fourth.setter
        def sv_type_fourth(self, string):
            """comment"""
            self.__sv_type_fourth = string

        @property
        def bather_bonus(self):
            """comment"""
            return self.__bather_bonus

        @bather_bonus.setter
        def bather_bonus(self, value):
            """comment"""
            self.__bather_bonus = value

        @property
        def donation(self):
            """comment"""
            return self.__donation

        @donation.setter
        def donation(self, value):
            """comment"""
            self.__donation = value

        @property
        def temple_bonus(self):
            """comment"""
            return self.__temple_bonus

        @temple_bonus.setter
        def temple_bonus(self, value):
            """comment"""
            self.__temple_bonus = value

        @property
        def chatterbox_bonus(self):
            """comment"""
            return self.__chatterbox_bonus

        @chatterbox_bonus.setter
        def chatterbox_bonus(self, value):
            """comment"""
            self.__chatterbox_bonus = value

        @property
        def collector_bonus(self):
            """comment"""
            return self.__collector_bonus

        @collector_bonus.setter
        def collector_bonus(self, value):
            """comment"""
            self.__collector_bonus = value

        @property
        def gourmet_bonus(self):
            """comment"""
            return self.__gourmet_bonus

        @gourmet_bonus.setter
        def gourmet_bonus(self, value):
            """comment"""
            self.__gourmet_bonus = value
