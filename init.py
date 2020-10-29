#!/usr/bin/python3
"""board initializing"""
from deck import Card, Deck, HotSpring, Encounter, Meal, Souvenir
from player import Player


HS1 = HotSpring("Hot Spring", 2, "Hot Spring")
HS2 = HotSpring("Hot Spring", 2, "Hot Spring")
HS3 = HotSpring("Hot Spring", 2, "Hot Spring")
HS4 = HotSpring("Hot Spring", 2, "Hot Spring")
HS5 = HotSpring("Hot Spring", 2, "Hot Spring")
HS6 = HotSpring("Hot Spring", 2, "Hot Spring")
HS7 = HotSpring("Hot Spring", 3, "Hot Spring")
HS8 = HotSpring("Hot Spring", 3, "Hot Spring")
HS9 = HotSpring("Hot Spring", 3, "Hot Spring")
HS10 = HotSpring("Hot Spring", 3, "Hot Spring")
HS11 = HotSpring("Hot Spring", 3, "Hot Spring")
HS12 = HotSpring("Hot Spring", 3, "Hot Spring")

HSlist = []
HSDeck = Deck(0, HSlist)
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


ENC1 = Encounter("Encounter", 0, "Kuge")
ENC2 = Encounter("Encounter", 0, "Kuge")
ENC3 = Encounter("Encounter", 0, "Miko")
ENC4 = Encounter("Encounter", 0, "Miko")
ENC5 = Encounter("Enounter", 3, "Samurai")
ENC6 = Encounter("Encounter", 3, "Samurai")
ENC7 = Encounter("Encounter", 0, "Shokunin")
ENC8 = Encounter("Encounter", 0, "Shokunin")
ENC9 = Encounter("Encounter", 0, "Annaibito: Paddy")
ENC10 = Encounter("Encounter", 0, "Annaibito: Paddy")
ENC11 = Encounter("Encounter", 0, "Annaibito: Mountain")
ENC12 = Encounter("Encounter", 0, "Annaibito: Mountain")
ENC13 = Encounter("Encounter", 0, "Annaibito: Sea")
ENC14 = Encounter("Encounter", 0, "Annaibito: Sea")

ENClist = []
ENCDeck = Deck(0, ENClist)
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


M1 = Meal("Meal", 6, "Misoshiru", 1)
M2 = Meal("Meal", 6, "Misoshiru", 1)
M3 = Meal("Meal", 6, "Misoshiru", 1)
M4 = Meal("Meal", 6, "Dango", 1)
M5 = Meal("Meal", 6, "Dango", 1)
M6 = Meal("Meal", 6, "Dango", 1)
M7 = Meal("Meal", 6, "Nigirimeshi", 1)
M8 = Meal("Meal", 6, "Nigirimeshi", 1)
M9 = Meal("Meal", 6, "Nigirimeshi", 1)
M10 = Meal("Meal", 6, "Tempura", 2)
M11 = Meal("Meal", 6, "Tempura", 2)
M12 = Meal("Meal", 6, "Soba", 2)
M13 = Meal("Meal", 6, "Soba", 2)
M14 = Meal("Meal", 6, "Yakitori", 2)
M15 = Meal("Meal", 6, "Yakitori", 2)
M16 = Meal("Meal", 6, "Tofu", 2)
M17 = Meal("Meal", 6, "Tofu", 2)
M18 = Meal("Meal", 6, "Sushi", 2)
M19 = Meal("Meal", 6, "Sushi", 2)
M20 = Meal("Meal", 6, "Fugu", 3)
M21 = Meal("Meal", 6, "Donburi", 3)
M22 = Meal("Meal", 6, "Sashimi", 3)
M23 = Meal("Meal", 6, "Udon", 3)
M24 = Meal("Meal", 6, "Unagi", 3)
M25 = Meal("Meal", 6, "Tai Meshi", 3)

Mlist = []
MDeck = Deck(0, Mlist)
MDeck.add(M1)
MDeck.add(M2)
MDeck.add(M3)
MDeck.add(M4)
MDeck.add(M5)
MDeck.add(M6)
MDeck.add(M7)
MDeck.add(M8)
MDeck.add(M9)
MDeck.add(M10)
MDeck.add(M11)
MDeck.add(M12)
MDeck.add(M13)
MDeck.add(M14)
MDeck.add(M15)
MDeck.add(M16)
MDeck.add(M17)
MDeck.add(M18)
MDeck.add(M19)
MDeck.add(M20)
MDeck.add(M21)
MDeck.add(M22)
MDeck.add(M23)
MDeck.add(M24)
MDeck.add(M25)


SV1 = Souvenir("Souvenir", 1, "Gofu", "Small Item", 1)
SV2 = Souvenir("Souvenir", 1, "Koma", "Small Item", 1)
SV3 = Souvenir("Souvenir", 1, "Yunomi", "Small Item", 1)
SV4 = Souvenir("Souvenir", 1, "Washi", "Small Item", 1)
SV5 = Souvenir("Souvenir", 1, "Uchiwa", "Small Item", 1)
SV6 = Souvenir("Souvenir", 1, "Hashi", "Small Item", 1)
SV7 = Souvenir("Souvenir", 1, "Konpeito", "Food and Drink", 1)
SV8 = Souvenir("Souvenir", 1, "Kamaboko", "Food and Drink", 1)
SV9 = Souvenir("Souvenir", 1, "Manju", "Food and Drink", 1)
SV10 = Souvenir("Souvenir", 1, "Daifuku", "Food and Drink", 2)
SV11 = Souvenir("Souvenir", 1, "Ocha", "Food and Drink", 2)
SV12 = Souvenir("Souvenir", 1, "Sake", "Food and Drink", 2)
SV13 = Souvenir("Souvenir", 1, "Yukata", "Clothing", 2)
SV14 = Souvenir("Souvenir", 1, "Kan Zashi", "Clothing", 2)
SV15 = Souvenir("Souvenir", 1, "Geta", "Clothing", 2)
SV16 = Souvenir("Souvenir", 1, "Haori", "Clothing", 2)
SV17 = Souvenir("Souvenir", 1, "Furoshiki", "Clothing", 2)
SV18 = Souvenir("Souvenir", 1, "Sandogasa", "Clothing", 2)
SV19 = Souvenir("Souvenir", 1, "Netsuke", "Art", 2)
SV20 = Souvenir("Souvenir", 1, "Shikki", "Art", 2)
SV21 = Souvenir("Souvenir", 1, "Jubako", "Art", 2)
SV22 = Souvenir("Souvenir", 1, "Ukiyoe", "Art", 3)
SV23 = Souvenir("Souvenir", 1, "Sumie", "Art", 3)
SV24 = Souvenir("Souvenir", 1, "Shamisen", "Art", 3)

SVlist = []
SVDeck = Deck(0, SVlist)
SVDeck.add(SV1)
SVDeck.add(SV2)
SVDeck.add(SV3)
SVDeck.add(SV4)
SVDeck.add(SV5)
SVDeck.add(SV6)
SVDeck.add(SV7)
SVDeck.add(SV8)
SVDeck.add(SV9)
SVDeck.add(SV10)
SVDeck.add(SV11)
SVDeck.add(SV12)
SVDeck.add(SV13)
SVDeck.add(SV14)
SVDeck.add(SV15)
SVDeck.add(SV16)
SVDeck.add(SV17)
SVDeck.add(SV18)
SVDeck.add(SV19)
SVDeck.add(SV20)
SVDeck.add(SV21)
SVDeck.add(SV22)
SVDeck.add(SV23)
SVDeck.add(SV24)


Dlist = []
DiscardDeck = Deck(0, Dlist)

"""Player initialization"""
GreenList = []
GreenDeck = Deck(0, GreenList)
GreenPlayer = Player("Green", GreenDeck)

PurpleList = []
PurpleDeck = Deck(0, PurpleList)
PurplePlayer = Player("Purple", PurpleDeck)

YellowList = []
YellowDeck = Deck(0, YellowList)
YellowPlayer = Player("Yellow", YellowDeck)

BlueList = []
BlueDeck = Deck(0, BlueList)
BluePlayer = Player("Blue", BlueDeck)

GreyList = []
GreyDeck = Deck(0, GreyList)
GreyPlayer = Player("Grey", GreyDeck)

player_list = []    # active players global list
board_1_list = [] # order players finish board
board_2_list = []
board_3_list = []
board_4_list = []
current_player = None # initialize global current player tracker
