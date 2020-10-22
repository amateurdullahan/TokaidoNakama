#!/usr/bin/python3
"""location class and inherited stuff"""
import pygame
import pygame_menu
from player import Player
from deck import Card, Deck, HotSpring, Encounter, Meal, Souvenir
from init import HSDeck
from bonus_tracker import *


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
        player.score += player.pano_paddy
        pano_paddy_check(player)
        return (player)
    else:
        print("Max Paddy Panorama Has Been Reached")
        return (player)

def Pano_Mt_Loc(player):
    """mountain location function"""
    if player.pano_mt < 4:
        player.pano_mt += 1
        player.score += player.pano_mt
        pano_mt_check(player)
        return (player)
    else:
        print("Max Mountain Panorama Has Been Reached")
        return (player)

def Pano_Sea_Loc(player):
    """sea location function"""
    if player.pano_sea < 5:
        player.pano_sea += 1
        player.score += player.pano_sea
        pano_sea_check(player)
        return (player)
    else:
        print("Max Sea Panorama Has Been Reaced")
        return (player)

def Temple_Loc(player, num):
    """temple location function"""
    player.coins -= num
    player.score += num
    player = temple_bonus_check(player)
    return (player)

def Village_Loc(player, cardname):
    """Village location function TBW"""
    for a in range(len(SVDeck.card_list)):
        if SVDeck.card_list[a].name == cardname:
            bought = SVDeck.card_list[a]
            break
        a += 1
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
    MoveCard(player, SVDeck, bought)
    return (player)
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

def Inn_Loc(current_player, cardname):
    """inn location function TBW"""
    for a in range(len(MDeck.card_list)):
        if MDeck.card_list[a].name == cardname:
            meal = MDeck.card_list[a]
            break
            a += 1
    MoveCard(player, MDeck, meal)
    return (player)

def Encounter_Loc(current_player, cardname):
    """encounter location function TBW"""
    for a in range(len(ENCDeck.card_list)):
        if ENCDeck.card_list[a].name == cardname:
            encounter = ENCDeck.card_list[a]
            break
            a += 1
    MoveCard(player, ENCDeck, encounter)
    return (player)

def discard(deck, cardname):
    """discard function"""
    from init import DiscardDeck
    for a in range(len(deck.card_list)):
        if deck.card_list[a].name == cardname:
            DiscardDeck.add(deck.card_list.pop(a))
            deck.number_of_cards -= 1
            return
        a += 1
