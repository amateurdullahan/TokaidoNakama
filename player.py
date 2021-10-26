#!/usr/bin/python3
"""Handles the player objects and their associated attributes."""
from deck import Deck


class Player():
        def __init__(self, color="", playerdeck=Deck(), score=0, coins=7,
                     board_space=99, pano_paddy=0, pano_mt=0, pano_sea=0,
                     sv_type_first="", sv_type_second="", sv_type_third="",
                     sv_type_fourth="", bather_bonus=0, icon=0, donation=0,
                     temple_bonus=0, chatterbox_bonus=0, collector_bonus=0,
                     gourmet_bonus=0):
            """Player object intialization."""
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
            """Player's color. Can be green, blue, yellow, purple, or grey."""
            return self.__color

        @color.setter
        def color(self, string):
            """Sets the player's color from green, blue, yellow, purple,
            or grey."""
            self.__color = string

        @property
        def score(self):
            """Player's score."""
            return self.__score

        @score.setter
        def score(self, value):
            """Sets the player's score."""
            self.__score = value

        @property
        def coins(self):
            """Player's coin count."""
            return self.__coins

        @coins.setter
        def coins(self, value):
            """Sets the player's coin count."""
            self.__coins = value

        @property
        def board_space(self):
            """The player's current location on the board."""
            return self.__board_space

        @board_space.setter
        def board_space(self, value):
            """Sets the player's location on the board."""
            self.__board_space = value

        @property
        def pano_paddy(self):
            """Player's padfield panoramic count (3 max)."""
            return self.__pano_paddy

        @pano_paddy.setter
        def pano_paddy(self, value):
            """Sets the player's padfield panoramic count (3 max)."""
            self.__pano_paddy = value

        @property
        def pano_mt(self):
            """Player's mountain panoramic count (4 max)."""
            return self.__pano_mt

        @pano_mt.setter
        def pano_mt(self, value):
            """Sets the player's mountain panoramic count (4 max)."""
            self.__pano_mt = value

        @property
        def pano_sea(self):
            """Player's sea panoramic count (5 max)."""
            return self.__pano_sea

        @pano_sea.setter
        def pano_sea(self, value):
            """Sets the player's sea panoramic count (5 max)."""
            self.__pano_sea = value

        @property
        def sv_type_first(self):
            """Player's first souvenir type acquired."""
            return self.__sv_type_first

        @sv_type_first.setter
        def sv_type_first(self, string):
            """Sets the souvenir type the player acquired first."""
            self.__sv_type_first = string

        @property
        def sv_type_second(self):
            """Player's second souvenir type acquired."""
            return self.__sv_type_second

        @sv_type_second.setter
        def sv_type_second(self, string):
            """Sets the souvenir type the player acquired second."""
            self.__sv_type_second = string

        @property
        def sv_type_third(self):
            """Player's third souvenir type acquired."""
            return self.__sv_type_third

        @sv_type_third.setter
        def sv_type_third(self, string):
            """Sets the souvenir type the player acquired third."""
            self.__sv_type_third = string

        @property
        def sv_type_fourth(self):
            """Player's final souvenir type acquired."""
            return self.__sv_type_fourth

        @sv_type_fourth.setter
        def sv_type_fourth(self, string):
            """Sets the souvenir type the player acquired last."""
            self.__sv_type_fourth = string

        @property
        def bather_bonus(self):
            """Bather achievement flag."""
            return self.__bather_bonus

        @bather_bonus.setter
        def bather_bonus(self, value):
            """Sets Bather achievement flag for the player."""
            self.__bather_bonus = value

        @property
        def donation(self):
            """Player's total donated amount of coins."""
            return self.__donation

        @donation.setter
        def donation(self, value):
            """Sets the player's total donation amount."""
            self.__donation = value

        @property
        def temple_bonus(self):
            """Player's placement in the temple donation amount bonus."""
            return self.__temple_bonus

        @temple_bonus.setter
        def temple_bonus(self, value):
            """Sets the player's placement for the temple donation
            amount bonus."""
            self.__temple_bonus = value

        @property
        def chatterbox_bonus(self):
            """Chatterbox achievement flag."""
            return self.__chatterbox_bonus

        @chatterbox_bonus.setter
        def chatterbox_bonus(self, value):
            """Sets Chatterbox achievement flag for the player."""
            self.__chatterbox_bonus = value

        @property
        def collector_bonus(self):
            """Collector achievement flag."""
            return self.__collector_bonus

        @collector_bonus.setter
        def collector_bonus(self, value):
            """Sets Collector achievement flag for the player."""
            self.__collector_bonus = value

        @property
        def gourmet_bonus(self):
            """Gourmet achievement flag."""
            return self.__gourmet_bonus

        @gourmet_bonus.setter
        def gourmet_bonus(self, value):
            """Sets Gourmet achievement flag for the player."""
            self.__gourmet_bonus = value
