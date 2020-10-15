#!/usr/bin/python3
"""location class and inherited stuff"""


""" NOT SURE WE NEED THIS
class Location():
    base location
    def __init__(self, board_space, name="", func):
        self.board_space = board_space
        self.name = name
        self.func = func

    @property
    def board_space(self):
        return self.__boardspace

    @board_space.setter
    def board_space(self, pygame_rect):
        self.__boardspace = pygame_rect

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, string):
        self.__name = string

    @property
    def func(self):
        return self.__func

    @func.setter
    def func(self, function)
        self.__func = function"""

def Farm_Loc(Player):
    """farm location function"""
    return Player.coins += 3

def Panorama_Paddy_Loc(Player):
    """paddy location function"""
    Player.pano_paddy += 1
    Player.points += Player.pano_paddy
    """achievment check"""

def Panorama_Mountain_Loc(Player):
    """mountain location function"""
    Player.pano_mt += 1
    Player.points += Player.pano_mt
    """achievment check"""

def Panorama_Sea_Loc(Player):
    """sea location function"""
    Player.pano_sea += 1
    Player.points += Player.pano_sea
    """achievment check"""

def Temple_Loc(Player):
    """temple location function TBW"""
    Player.coins -= 1 """actual number will be player input"""

def Souvenir_Shop_Loc(Player):
    """souvenirshop location function TBW"""

def Hot_Spring_Loc(Player):
    """hot spring location function TBW"""

def Inn_Loc(Player):
    """inn location function TBW"""

def Encounter_Loc(Player):
    """encounter location function TBW"""
