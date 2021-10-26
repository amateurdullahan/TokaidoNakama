#!/usr/bin/python3
"""location class"""
import pygame
import pygame_menu
from player import Player
from deck import *
from init import *


def MoveCard(player, deck, card):
    """method to move cards between decks"""
    for idx in range(len(deck.card_list)):
        if deck.card_list[idx] is card:
            player.playerdeck.add(deck.card_list.pop(idx))
            deck.number_of_cards -= 1
            break

def Farm_Loc(player):
    """farm location function"""
    player.coins += 3
    return (player)


def Pano_Paddy_Loc(player):
    """paddy location function"""
    if player.pano_paddy < 3:
        player.pano_paddy += 1
        player.score += player.pano_paddy
        # pano_paddy_check(player) for acheivements
        return (player)
    else:
        print("Max Paddy Panorama Has Been Reached")
        return (player)

def Pano_Mt_Loc(player):
    """mountain location function"""
    if player.pano_mt < 4:
        player.pano_mt += 1
        player.score += player.pano_mt
        # pano_mt_check(player) for acheivements
        return (player)
    else:
        print("Max Mountain Panorama Has Been Reached")
        return (player)

def Pano_Sea_Loc(player):
    """sea location function"""
    if player.pano_sea < 5:
        player.pano_sea += 1
        player.score += player.pano_sea
        # pano_sea_check(player) for acheivements
        return (player)
    else:
        print("Max Sea Panorama Has Been Reached")
        return (player)

def Temple_Loc(player, num):
    """temple location function"""
    player.coins -= num
    player.score += num
    player.donation += num
    # player = temple_bonus_check(player) for acheivements
    return (player)

def Village_Loc(player, cardname):
    """Village location function"""
    print("Card name:", cardname)
    for idx in range(len(SVDeck.card_list)):
        print("Card checked in loop:", SVDeck.card_list[idx].name)
        if SVDeck.card_list[idx].name == cardname:
            bought = SVDeck.card_list[idx]
            break
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
    # collector_bonus_check(player) for acheivements
    return (player)

def Hot_Spring_Loc(player, pts):
    """hot spring location function"""
    if pts == 2:
        print("2 points clicked")
        for idx in range(len(HSDeck.card_list)):
            if HSDeck.card_list[idx].point_value == 2:
                print("2 Points Selected")
                player.playerdeck.add(HSDeck.card_list.pop(idx))
                player.score += 2
                HSDeck.number_of_cards -= 1
                # player = bather_bonus_check(player) for acheivements
                return (player)
    elif pts == 3:
        print("3 points clicked")
        for idx in range(len(HSDeck.card_list)):
            if HSDeck.card_list[idx].point_value == 3:
                player.playerdeck.add(HSDeck.card_list.pop(idx))
                player.score += 3
                HSDeck.number_of_cards -= 1
                # player = bather_bonus_check(player) for acheivements
                return (player)

def Inn_Loc(player, cardname):
    """inn location function"""
    if cardname == 'Skip':
        return(player)
    for idx in range(len(MDeck.card_list)):
        print("Card Name:", cardname)
        print("Card Checked:", MDeck.card_list[idx].name)
        if MDeck.card_list[idx].name == cardname:
            meal = MDeck.card_list[idx]
            break
    player.score += 6
    player.coins -= MDeck.card_list[idx].cost
    MoveCard(player, MDeck, meal)
    # discard unchosen meal cards
    # player = gourmet_bonus_check(player) for acheivements
    return (player)

def Encounter_Loc(player, cardname):
    """encounter location function"""
    for idx in range(len(ENCDeck.card_list)):
        if ENCDeck.card_list[idx].name == cardname:
            encounter = ENCDeck.card_list[idx]
            break
    MoveCard(player, ENCDeck, encounter)
    # chatterbox_bonus_check(player) for acheivements
    if cardname == "Kuge":
        player.coins += 3
    if cardname == "Samurai":
        player.score += 3
    if cardname == "Miko":
        player.donation += 1
        player.score += 1
        # temple_bonus_check(player) for acheivements
    if cardname == "Annaibito: Paddy":
        if player.pano_paddy < 3:
            player.pano_paddy += 1
            player.score += player.pano_paddy
            # pano_paddy_check(player) for acheivements
        else:
            print("Max Paddy Panorama Has Been Reached")
    if cardname == "Annaibito: Mountain":
        if player.pano_mt < 4:
            player.pano_mt += 1
            player.score += player.pano_mt
            # pano_mt_check(player) for acheivements
        else:
            print("Max Mountain Panorama Has Been Reached")
    if cardname == "Annaibito: Sea":
        if player.pano_sea < 3:
            player.pano_sea += 1
            player.score += player.pano_sea
            # pano_sea_check(player) for acheivements
        else:
            print("Max Sea Panorama Has Been Reached")
    return (player)

def discard(deck, cardname):
    """discard function"""
    from init import DiscardDeck
    for idx in range(len(deck.card_list)):
        if deck.card_list[idx].name == cardname:
            DiscardDeck.add(deck.card_list.pop(idx))
            deck.number_of_cards -= 1
            return
