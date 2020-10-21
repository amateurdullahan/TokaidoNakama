#!/usr/bin/python3
"""location class and inherited stuff"""
import pygame
import pygame_menu
from player import Player
from deck import Card, Deck, HotSpring, Encounter, Meal, Souvenir
from init import HSDeck, GreenPlayer

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


def MoveCard(player, deck, card):
    """method to move cards between decks"""
    for a in range(len(deck.card_list)):
        if deck.card_list[a] is card:
            player.playerdeck.add(deck.card_list.pop(a))
            deck.number_of_cards -= 1
            break
        a += 1

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

def Village_Loc(Player, Deck, Discard):
    """Village location function TBW"""
    """bought will be the Card obj they select"""
    while a < 3:
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


def Hot_Spring_Loc(current_player, pts):
    """hot spring location function TBW"""
    if pts == 2:
        print("2 points clicked")
        for a in range(len(HSDeck.card_list)):
            if HSDeck.card_list[a].point_value == 2:
                print("2 Points Selected")
                current_player.playerdeck.add(HSDeck.card_list.pop(a))
                HSDeck.number_of_cards -= 1
                break
            a += 1
    elif pts == 3:
        print("3 points clicked")
        for a in range(len(HSDeck.card_list)):
            if HSDeck.card_list[a].point_value == 3:
                GreenPlayer.playerdeck.add(HSDeck.card_list.pop(a))
                HSDeck.number_of_cards -= 1
                break
            a += 1


def Inn_Loc(Player, Deck):
    """inn location function TBW"""
    meal = """"whatever they select"""
    MoveCard(Player, Deck, meal)

def Encounter_Loc(Player, Deck):
    """encounter location function TBW"""
    encounter = """whatever they select"""
    MoveCard(Player, Deck, encounter)
