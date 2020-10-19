#!/usr/bin/python3
"""deck objects"""

class Card():
        def __init__(self, type="", point_value=0, name=""):
            """initializing the cards"""
            self.type = type
            self.point_value = point_value
            self.name = name

        @property
        def type(self):
            """comment"""
            return self.__type

        @type.setter
        def type(self, string):
            """comment"""
            self.__type = string

        @property
        def point_value(self):
            """comment"""
            return self.__point_value

        @point_value.setter
        def point_value(self, value):
            """comment"""
            self.__point_value = value

        @property
        def name(self):
            """comment"""
            return self.__name


        @name.setter
        def name(self, string):
            """comment"""
            self.__name = string

        def __str__(self):
            """string rep"""
            return "[{:s}] points = {:d}, name = {:s}".format(self.type, self.point_value, self.name)

class HotSpring(Card):
        def __init__(self, type="", point_value=0, name=""):
            super().__init__(type, point_value, name)

class Encounter(Card):
        def __init__(self, type="", point_value=0, name=""):
            super().__init__(type, point_value, name)

class Meal(Card):
        def __init__(self, type="", point_value=0, name="", cost=0):
            self.type = type
            self.point_value = point_value
            self.name = name
            self.cost = cost

        @property
        def type(self):
            """comment"""
            return self.__type

        @type.setter
        def type(self, string):
            """comment"""
            self.__type = string

        @property
        def point_value(self):
            """comment"""
            return self.__point_value

        @point_value.setter
        def point_value(self, value):
            """comment"""
            self.__point_value = value

        @property
        def name(self):
            """comment"""
            return self.__name

        @name.setter
        def name(self, string):
            """comment"""
            self.__name = string

        @property
        def cost(self):
            """comment"""
            return self.__cost

        @cost.setter
        def cost(self, value):
            """comment"""
            self.__cost = value

        def __str__(self):
            """string rep"""
            return "[{:s}] points = {:d}, name = {:s}, cost = {:d}".format(self.type, self.point_value, self.name, self.cost)

class Souvenir(Card):
        def __init__(self, type="", point_value=0, name="", subtype="", cost=0):
            self.type = type
            self.point_value = point_value
            self.name = name
            self.subtype = subtype
            self.cost = cost

        @property
        def type(self):
            """comment"""
            return self.__type

        @type.setter
        def type(self, string):
            """comment"""
            self.__type = string

        @property
        def point_value(self):
            """comment"""
            return self.__point_value

        @point_value.setter
        def point_value(self, value):
            """comment"""
            self.__point_value = value

        @property
        def name(self):
            """comment"""
            return self.__name


        @name.setter
        def name(self, string):
            """comment"""
            self.__name = string

        @property
        def subtype(self):
            """comment"""
            return self.__subtype

        @subtype.setter
        def subtype(self, string):
            self.__subtype = string

        @property
        def cost(self):
            """comment"""
            return self.__cost

        @cost.setter
        def cost(self, value):
            """comment"""
            self.__cost = value

        def __str__(self):
            """string rep"""
            return "[{:s}] points = {:d}, name = {:s}, subtype = {:s}, cost = {:d}".format(self.type, self.point_value, self.name, self.subtype, self.cost)

class Deck():
        def __init__(self, number_of_cards=0, card_list=[]):
            """initializing a deck, board or player owned"""
            self.number_of_cards = number_of_cards
            self.card_list = card_list

        def add(self, obj):
            """add card to deck"""
            self.card_list.append(obj)
            self.number_of_cards += 1


        def print_list(self):
            for a in range(len(self.card_list)):
                print(self.card_list[a])
                a += 1
