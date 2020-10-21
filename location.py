#!/usr/bin/python3
"""location class and inherited stuff"""
import pygame
import pygame_menu
from player import Player
from deck import Card, Deck, HotSpring, Encounter, Meal, Souvenir
from init import HSDeck

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

def Farm_Loc(player):
    """farm location function"""
    player.coins += 3
    return (player)


def Pano_Paddy_Loc(player):
    """paddy location function"""
    if player.pano_paddy < 3:
        player.pano_paddy += 1
        player.points += player.pano_paddy
        # pano_paddy_check(player)
        return (player)

def Pano_Mt_Loc(player):
    """mountain location function"""
    if player.pano_mt < 4:
        player.pano_mt += 1
        player.points += player.pano_mt
        """achievment check"""
        return (player)

def Pano_Sea_Loc(player):
    """sea location function"""
    if player.pano_sea < 5:
        player.pano_sea += 1
        player.points += player.pano_sea
        """achievment check"""
        return (player)

def Temple_Loc(player):
    """temple location function TBW"""
    """Ask player for num of coins"""
    player.coins -= num
    player.score += num
    """ temple bonus check"""

def Village_Loc(player, Deck, Discard):
    """Village location function TBW"""
    """bought will be the Card obj they select"""
    while a < 3:
        """ask player which cards bought, do this three times"""
        if discard:
            Discard.add(bought)
        else:
            player.coins -= bought.cost
            if player.sv_type_first is "":
                player.sv_type_first = bought.subtype
                player.score += 1
            elif player.sv_type_first == bought.subtype:
                player.score += 1
            elif player.sv_type_second is "":
                player.sv_type_second = bought.subtype
                player.score += 3
            elif player.sv_type_second == bought.subtype:
                player.score += 3
            elif player.sv_type_third is "":
                player.sv_type_third = bought.subtype
                player.score += 5
            elif player.sv_type_third == bought.subtype:
                player.score += 5
            elif player.sv_type_fourth is "":
                player.sv_type_fourth = bought.subtype
                player.score += 7
            elif player.sv_type_fourth == bought.subtype:
                player.score += 7
            MoveCard(player, Deck, bought)
        """check collector acheviement"""

def Hot_Spring_Loc(player, pts):
    """hot spring location function TBW"""
    if pts == 2:
        print("2 points clicked")
        for a in range(len(HSDeck.card_list)):
            if HSDeck.card_list[a].point_value == 2:
                print("2 Points Selected")
                player.playerdeck.add(HSDeck.card_list.pop(a))
                player.score += 2
                HSDeck.number_of_cards -= 1
                return (player)
            a += 1
    elif pts == 3:
        print("3 points clicked")
        for a in range(len(HSDeck.card_list)):
            if HSDeck.card_list[a].point_value == 3:
                player.playerdeck.add(HSDeck.card_list.pop(a))
                player.score += 3
                HSDeck.number_of_cards -= 1
                return (player)
            a += 1

def Inn_Loc(current_player):
    """inn location function TBW"""
    meal = """"whatever they select"""
    MoveCard(player, Deck, meal)

def Encounter_Loc(player, Deck):
    """encounter location function TBW"""
    encounter = """whatever they select"""
    MoveCard(player, Deck, encounter)
