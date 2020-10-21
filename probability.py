#!/usr/bin/python3
"""all the probability funstuff"""
from deck import Deck, Card


def CostProb(Deck):
    """Determine Cost Probability"""
    cost1sum = 0
    cost2sum = 0
    cost3sum = 0
    for a in range(len(Deck.card_list)):
        if Deck.card_list[a].cost == 1:
            cost1sum += 1
        elif Deck.card_list[a].cost == 2:
            cost2sum += 1
        elif Deck.card_list[a].cost == 3:
            cost3sum += 1
        else:
            continue
        a += 1
    cost1sum = round(((cost1sum / Deck.number_of_cards) * 100), 2)
    cost2sum = round(((cost2sum / Deck.number_of_cards) * 100), 2)
    cost3sum = round(((cost3sum / Deck.number_of_cards) * 100), 2)
    return(cost1sum, cost2sum, cost3sum)

def PointProb(Deck):
    """Determine point prob"""
    point2sum = 0
    point3sum = 0
    for a in range(len(Deck.card_list)):
        if Deck.card_list[a].point_value == 2:
            point2sum += 1
        elif Deck.card_list[a].point_value == 3:
            point3sum += 1
        else:
            continue
        a += 1
    point2sum = round(((point2sum / Deck.number_of_cards) * 100), 2)
    point3sum = round(((point3sum / Deck.number_of_cards) * 100), 2)
    return(point2sum, point3sum)


def SubTypeProb(Deck):
    """determine subtype prob"""
    small_item_sum = 0
    food_drink_sum = 0
    clothing_sum = 0
    art_sum = 0
    for a in range(len(Deck.card_list)):
        if Deck.card_list[a].subtype == "Small Item":
            small_item_sum += 1
        elif Deck.card_list[a].subtype == "Food and Drink":
            food_drink_sum += 1
        elif Deck.card_list[a].subtype == "Clothing":
            clothing_sum += 1
        elif Deck.card_list[a].subtype == "Art":
            art_sum += 1
        else:
            continue
    small_item_sum = round(((small_item_sum / Deck.number_of_cards) * 100), 2)
    food_drink_sum = round(((food_drink_sum / Deck.number_of_cards) * 100), 2)
    clothing_sum = round(((clothing_sum / Deck.number_of_cards) * 100), 2)
    art_sum = round(((art_sum / Deck.number_of_cards) * 100), 2)
    return(small_item_sum, food_drink_sum, clothing_sum, art_sum)

def EncTypeProb(Deck):
    """encounter type probability"""
    kuge_sum = 0
    miko_sum = 0
    samurai_sum = 0
    shokunin_sum = 0
    anna_paddy_sum = 0
    anna_mtn_sum = 0
    anna_sea_sum = 0
    for a in range(len(Deck.card_list)):
        if Deck.card_list[a].name == "Kuge":
            kuge_sum += 1
        elif Deck.card_list[a].name == "Miko":
            miko_sum += 1
        elif Deck.card_list[a].name == "Samurai":
            samurai_sum += 1
        elif Deck.card_list[a].name == "Shoukunin":
            shokunin_sum += 1
        elif Deck.card_list[a].name == "Annaibito: Paddy":
            anna_paddy_sum += 1
        elif Deck.card_list[a].name == "Annaibito: Mountain":
            anna_mtn_sum += 1
        elif Deck.card_list[a].name == "Annaibito: Sea":
            anna_sea_sum += 1
        else:
            continue
        a += 1
    kuge_sum = round(((kuge_sum / Deck.number_of_cards) * 100), 2)
    miko_sum = round(((miko_sum / Deck.number_of_cards) * 100), 2)
    samurai_sum = round(((samurai_sum / Deck.number_of_cards) * 100), 2)
    shokunin_sum = round(((shokunin_sum / Deck.number_of_cards) * 100), 2)
    anna_paddy_sum = round(((anna_paddy_sum / Deck.number_of_cards) * 100), 2)
    anna_mtn_sum = round(((anna_mtn_sum / Deck.number_of_cards) * 100), 2)
    anna_sea_sum = round(((anna_sea_sum / Deck.number_of_cards) * 100), 2)
    return(kuge_sum, miko_sum, samurai_sum, shokunin_sum, anna_paddy_sum, anna_mtn_sum, anna_sea_sum)
