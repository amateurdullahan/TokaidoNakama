#!/usr/bin/python3
"""all the probability functions"""
from deck import Deck, Card


def CostProb(Deck):
    """Determine Cost probability"""
    cost1sum = 0
    cost2sum = 0
    cost3sum = 0
    cost_list = []
    for idx in range(len(Deck.card_list)):
        if Deck.card_list[idx].cost == 1:
            cost1sum += 1
        elif Deck.card_list[idx].cost == 2:
            cost2sum += 1
        elif Deck.card_list[idx].cost == 3:
            cost3sum += 1
        else:
            continue
    cost1sum = round(((cost1sum / Deck.number_of_cards) * 100), 2)
    cost2sum = round(((cost2sum / Deck.number_of_cards) * 100), 2)
    cost3sum = round(((cost3sum / Deck.number_of_cards) * 100), 2)
    cost_list.append(cost1sum)
    cost_list.append(cost2sum)
    cost_list.append(cost3sum)
    return(cost_list)

def PointProb(Deck):
    """Determine Point probability"""
    point2sum = 0
    point3sum = 0
    point_list = []
    for idx in range(len(Deck.card_list)):
        if Deck.card_list[idx].point_value == 2:
            point2sum += 1
        elif Deck.card_list[idx].point_value == 3:
            point3sum += 1
        else:
            continue
    point2sum = round(((point2sum / Deck.number_of_cards) * 100), 2)
    point3sum = round(((point3sum / Deck.number_of_cards) * 100), 2)
    point_list.append(point2sum)
    point_list.append(point3sum)
    return(point_list)


def SubTypeProb(Deck):
    """Determine Subtype probability"""
    small_item_sum = 0
    food_drink_sum = 0
    clothing_sum = 0
    art_sum = 0
    type_list = []
    for idx in range(len(Deck.card_list)):
        if Deck.card_list[idx].subtype == "Small Item":
            small_item_sum += 1
        elif Deck.card_list[idx].subtype == "Food and Drink":
            food_drink_sum += 1
        elif Deck.card_list[idx].subtype == "Clothing":
            clothing_sum += 1
        elif Deck.card_list[idx].subtype == "Art":
            art_sum += 1
        else:
            continue
    small_item_sum = round(((small_item_sum / Deck.number_of_cards) * 100), 2)
    food_drink_sum = round(((food_drink_sum / Deck.number_of_cards) * 100), 2)
    clothing_sum = round(((clothing_sum / Deck.number_of_cards) * 100), 2)
    art_sum = round(((art_sum / Deck.number_of_cards) * 100), 2)
    type_list.append(small_item_sum)
    type_list.append(food_drink_sum)
    type_list.append(clothing_sum)
    type_list.append(art_sum)
    return(type_list)

def EncTypeProb(Deck):
    """Determine Encounter Type probability"""
    kuge_sum = 0
    miko_sum = 0
    samurai_sum = 0
    shokunin_sum = 0
    anna_paddy_sum = 0
    anna_mtn_sum = 0
    anna_sea_sum = 0
    type_list = []
    for idx in range(len(Deck.card_list)):
        if Deck.card_list[idx].name == "Kuge":
            kuge_sum += 1
        elif Deck.card_list[idx].name == "Miko":
            miko_sum += 1
        elif Deck.card_list[idx].name == "Samurai":
            samurai_sum += 1
        elif Deck.card_list[idx].name == "Shokunin":
            shokunin_sum += 1
        elif Deck.card_list[idx].name == "Annaibito: Paddy":
            anna_paddy_sum += 1
        elif Deck.card_list[idx].name == "Annaibito: Mountain":
            anna_mtn_sum += 1
        elif Deck.card_list[idx].name == "Annaibito: Sea":
            anna_sea_sum += 1
        else:
            continue
    kuge_sum = round(((kuge_sum / Deck.number_of_cards) * 100), 2)
    miko_sum = round(((miko_sum / Deck.number_of_cards) * 100), 2)
    samurai_sum = round(((samurai_sum / Deck.number_of_cards) * 100), 2)
    shokunin_sum = round(((shokunin_sum / Deck.number_of_cards) * 100), 2)
    anna_paddy_sum = round(((anna_paddy_sum / Deck.number_of_cards) * 100), 2)
    anna_mtn_sum = round(((anna_mtn_sum / Deck.number_of_cards) * 100), 2)
    anna_sea_sum = round(((anna_sea_sum / Deck.number_of_cards) * 100), 2)
    type_list.append(kuge_sum)
    type_list.append(miko_sum)
    type_list.append(samurai_sum)
    type_list.append(shokunin_sum)
    type_list.append(anna_paddy_sum)
    type_list.append(anna_mtn_sum)
    type_list.append(anna_sea_sum)
    return(type_list)
