#!/usr/bin/python3
"""deck objects"""

class Card:
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

        @tname.setter
        def name(self, string):
            """comment"""
            self.__name = string




class Deck():
        def __init__(self, number_of_cards=0, owner=""):
            """initializing a deck, board or player owned"""
            self.number_of_cards = number_of_cards
            self.owner = owner
