#!/usr/bin/python3
"""location class and inherited stuff"""
from player import Player
from deck import Card, Deck, HotSpring, Encounter, Meal, Souvenir, MoveCard

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
    Player.coins += 3

def Panorama_Paddy_Loc(Player):
    """paddy location function"""
    if player.pano_paddy < 3:
        Player.pano_paddy += 1
        Player.points += Player.pano_paddy
        pano_paddy_check(Player)

def Panorama_Mountain_Loc(Player):
    """mountain location function"""
    if Player.pano_mt < 4:
        Player.pano_mt += 1
        Player.points += Player.pano_mt
        """achievment check"""

def Panorama_Sea_Loc(Player):
    """sea location function"""
    if Player.pano_sea < 5:
        Player.pano_sea += 1
        Player.points += Player.pano_sea
        """achievment check"""

def Temple_Loc(Player):
    """temple location function TBW"""
    """Ask player for num of coins"""
    Player.coins -= num
    Player.score += num
    """ temple bonus check"""

def Souvenir_Shop_Loc(Player, Deck, Discard):
    """souvenirshop location function TBW"""
    """bought will be the Card obj they select"""
    while a less than 3:
        """ask player which cards bought, do this three times"""
        if discard:
            Discard.add(bought)
        else:
            Player.coins -= bought.cost
            if Player.sv_type_first is "":
                Player.sv_type_first = bought.subtype
                Player.score += 1
            elif Player.sv_type_first == bought.subtype:
                Player.score += 1
            elif Player.sv_type_second is "":
                Player.sv_type_second = bought.subtype
                Player.score += 3
            elif Player.sv_type_second == bought.subtype:
                Player.score += 3
            elif Player.sv_type_third is "":
                Player.sv_type_third = bought.subtype
                Player.score += 5
            elif Player.sv_type_third == bought.subtype:
                Player.score += 5
            elif Player.sv_type_fourth is "":
                Player.sv_type_fourth = bought.subtype
                Player.score += 7
            elif Player.sv_type_fourth == bought.subtype:
                Player.score += 7
            MoveCard(Player, Deck, bought)
        """check collector acheviement"""


def Hot_Spring_Loc(Player, Deck):
    """hot spring location function TBW"""
    selected = """whatever the fuck they select"""
    MoveCard(Player, Deck, selected)
    bather_bonus_check("""number of HS cards""")
    """move card to player deck"""

def Inn_Loc(Player, Deck):
    """inn location function TBW"""
    meal = """"whatever they select"""
    MoveCard(Player, Deck, meal)

def Encounter_Loc(Player, Deck):
    """encounter location function TBW"""
    encounter = """whatever they select"""
    MoveCard(Player, Deck, encounter)
