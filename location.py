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
    if player.pano_paddy < 3:
        Player.pano_paddy += 1
        Player.points += Player.pano_paddy
        """achievment check"""

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

def Souvenir_Shop_Loc(Player):
    """souvenirshop location function TBW"""
    """ask player which cards bought, do this three times"""
    if discard:
        """move card to discard deck"""
    else:
        Player.coins -= bought.cost
        if Player.sv_type0 is None:
           Player.sv_type0 = bought.subtype
        elif Player.sv_type0 == bought.subtype:
            Player.score += 1
        elif Player.sv_type1 is None:
            Player.sv_type1 = bought.subtype
        elif Player.sv_type1 == bought.subtype:
            Player.score += 3
        elif Player.sv_type2 is None:
            Player.sv_type2 = bought.subtype
        elif Player.sv_type2 == bought.subtype:
            Player.score += 5
        elif Player.sv_type3 is None:
            Player.sv_type3 = bought.subtype
        elif Player.sv_type3 == bought.subtype:
            Player.score += 7
        """move card to player deck"""
        """check collector acheviement"""
    

def Hot_Spring_Loc(Player):
    """hot spring location function TBW"""
    """ask player if 2 or 3 pts"""
    Player.score += pts
    """check Bather achievement"""
    """move card to player deck"""

def Inn_Loc(Player):
    """inn location function TBW"""

def Encounter_Loc(Player):
    """encounter location function TBW"""
