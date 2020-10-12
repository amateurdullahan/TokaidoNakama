#!/usr/bin/python3
"""board initializing"""
from deck import *

def CardSetup():
    """set up board"""
    HS1 = Card("Hot Spring", 2, "Hot Spring")
    HS2 = Card("Hot Spring", 2, "Hot Spring")
    HS3 = Card("Hot Spring", 2, "Hot Spring")
    HS4 = Card("Hot Spring", 2, "Hot Spring")
    HS5 = Card("Hot Spring", 2, "Hot Spring")
    HS6 = Card("Hot Spring", 2, "Hot Spring")
    HS7 = Card("Hot Spring", 3, "Hot Spring")
    HS8 = Card("Hot Spring", 3, "Hot Spring")
    HS9 = Card("Hot Spring", 3, "Hot Spring")
    HS10 = Card("Hot Spring", 3, "Hot Spring")
    HS11 = Card("Hot Spring", 3, "Hot Spring")
    HS12 = Card("Hot Spring", 3, "Hot Spring")

    HSDeck = Deck(12, "Board")
    HSDeck.add(HS1)
    HSDeck.add(HS2)
    HSDeck.add(HS3)
    HSDeck.add(HS4)
    HSDeck.add(HS5)
    HSDeck.add(HS6)
    HSDeck.add(HS7)
    HSDeck.add(HS8)
    HSDeck.add(HS9)
    HSDeck.add(HS10)
    HSDeck.add(HS11)
    HSDeck.add(HS12)

    ENC1 = Card("Encounter", 0, "Kuge")
    ENC2 = Card("Encounter", 0, "Kuge")
    ENC3 = Card("Encounter", 0, "Miko")
    ENC4 = Card("Encounter", 0, "Miko")
    ENC5 = Card("Enounter", 3, "Samurai")
    ENC6 = Card("Encounter", 3, "Samurai")
    ENC7 = Card("Encounter", 0, "Shokunin")
    ENC8 = Card("Encounter", 0, "Shokunin")
    ENC9 = Card("Encounter", 0, "Annaibito: Paddy")
    ENC10 = Card("Encounter", 0, "Annaibito: Paddy")
    ENC11 = Card("Encounter", 0, "Annaibito: Mountain")
    ENC12 = Card("Encounter", 0, "Annaibito: Mountain")
    ENC13 = Card("Encounter", 0, "Annaibito: Sea")
    ENC14 = Card("Encounter", 0, "Annaibito: Sea")

    ENCDeck = Deck(14, "Board")
    ENCDeck.add(ENC1)
    ENCDeck.add(ENC2)
    ENCDeck.add(ENC3)
    ENCDeck.add(ENC4)
    ENCDeck.add(ENC5)
    ENCDeck.add(ENC6)
    ENCDeck.add(ENC7)
    ENCDeck.add(ENC8)
    ENCDeck.add(ENC9)
    ENCDeck.add(ENC10)
    ENCDeck.add(ENC11)
    ENCDeck.add(ENC12)
    ENCDeck.add(ENC13)
    ENCDeck.add(ENC14)

    M1 = Card("Meal", 0, "Misoshiru")
    M2 = Card("Meal", 0, "Misoshiru")
    M3 = Card("Meal", 0, "Misoshiru")
    M4 = Card("Meal", 0, "Dango")
    M5 = Card("Meal", 0, "Dango")
    M6 = Card("Meal", 0, "Dango")
    M7 = Card("Meal", 0, "Nigirimeshi")
    M8 = Card("Meal", 0, "Nigirimeshi")
    M9 = Card("Meal", 0, "Nigirimeshi")
    
