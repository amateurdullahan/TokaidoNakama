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

class HotSpring(Card):
        def __init__(self, type="", point_value=0, name=""):
            super().__init__(type, point_value, name)

class Encounter(Card):
        def __init__(self, type="", point_value=0, name=""):
            super().__init__(type, point_value, name)

class Meal(Card):
        def __init__(self, type="", point_value=0, name=""):
            super().__init__(type, point_value, name)

class Souvenir(Card):
        def __init__(self, type="", point_value=0, name="", subtype=""):
            self.type = type
            self.point_value = point_value
            self.name = name
            self.subtype = subtype

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

class Deck():
        def __init__(self, number_of_cards=0, owner="", card_list=[]):
            """initializing a deck, board or player owned"""
            self.number_of_cards = number_of_cards
            self.owner = owner
            self.card_list = card_list

        def add(self, obj):
            """add card to deck"""
            self.card_list.append(obj)

        def print_list(self):
            """just a test method to print a deck"""
            print(self.card_list)
