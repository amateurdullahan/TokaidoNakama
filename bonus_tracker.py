#!/usr/bin/python3
"""achievement checking functions"""
from player import *


class Achievements():
        def __init__(self, pano_paddy_bonus="", pano_mt_bonus="", pano_sea_bonus="", gourmet_count=0, bather_count=0, chatterbox_count=0, collector_count=0, temple_bonus_first=1, temple_bonus_second=1, temple_bonus_third=1):
            """initializing the players"""
            self.pano_paddy_bonus = pano_paddy_bonus
            self.pano_mt_bonus = pano_mt_bonus
            self.pano_sea_bonus = pano_sea_bonus
            self.gourmet_count = gourmet_count
            self.bather_count = bather_count
            self.chatterbox_count = chatterbox_count
            self.collector_count = collector_count
            self.temple_bonus_first = temple_bonus_first
            self.temple_bonus_second = temple_bonus_second
            self.temple_bonus_third = temple_bonus_third

        @property
        def pano_paddy_bonus(self):
            """comment"""
            return self.__pano_paddy_bonus

        @pano_paddy_bonus.setter
        def pano_paddy_bonus(self, string):
            """comment"""
            self.__pano_paddy_bonus = string

        @property
        def pano_mt_bonus(self):
            """comment"""
            return self.__pano_mt_bonus

        @pano_mt_bonus.setter
        def pano_mt_bonus(self, string):
            """comment"""
            self.__pano_mt_bonus = string

        @property
        def pano_sea_bonus(self):
            """comment"""
            return self.__pano_sea_bonus

        @pano_sea_bonus
        def pano_sea_bonus(self, string):
            """comment"""
            self.__pano_sea_bonus = string

        @property
        def gourmet_count(self):
            """comment"""
            return self.__gourmet_count

        @gourmet_count.setter
        def gourmet_count(self, value):
            """comment"""
            self.__gourmet_count = value

        @property
        def bather_count(self):
            """comment"""
            return self.__bather_count

        @bather_count.setter
        def bather_count(self, value):
            """comment"""
            self.__bather_count = value

        @property
        def chatterbox_count(self):
            """comment"""
            return self.__chatterbox_count

        @chatterbox_count.setter
        def chatterbox_count(self, value):
            """comment"""
            self.__chatterbox_count = value

        @property
        def collector_count(self):
            """comment"""
            return self.__collector_count

        @collector_count.setter
        def collector_count(self, value):
            """comment"""
            self.__collector_count = value

        @property
        def temple_bonus_first=1(self):
            """comment"""
            return self.__temple_bonus_first

        @temple_bonus_first.setter
        def temple_bonus_first(self, value):
            """comment"""
            self.__temple_bonus_first = value

        @property
        def temple_bonus_second(self):
            """comment"""
            return self.__temple_bonus_second

        @temple_bonus_second.setter
        def temple_bonus_second(self, value):
            """comment"""
            self.__temple_bonus_second = value

        @property
        def temple_bonus_third(self):
            """comment"""
            return self.__temple_bonus_third

        @temple_bonus_third.setter
        def temple_bonus_third(self, value):
            """comment"""
            self.__temple_bonus_third = value

def pano_paddy_check(current_player):
    if pano_paddy_bonus == None:
        if current_player.pano_paddy == 3:
            pano_paddy_bonus = current_player
            current_player.score += 3

def pano_mt_check(current_player):
    if pano_mt_bonus == None:
        if current_player.pano_mt == 4:
            pano_mt_bonus = current_player
            current_player.score += 3

def pano_sea_check(current_player):
    if pano_sea_bonus == None:
        if current_player.pano_sea == 5:
            pano_sea_bonus = current_player
            current_player.score += 3

def bather_bonus_check(current_player):
    count = 0
    for a in range(len(current_player.playerdeck.card_list)):
        if current_player.playerdeck.card_list[a].type is HotSprings:
            count += 1
    if count > bather_count:
        bather_count = count
    for player in player_list:
        if player.bather_bonus = 0
            player_count = 0
            for a in range(len(player.playerdeck.card_list)):
                if player.playerdeck.card_list[a].type is HotSprings:
                    player_count += 1
            if player_count == bather_count:
                player.bather_bonus = 1
                player.score += 3
        elif player.bather_bonus == 1:
            player_count = 0
            for a in range(len(player.playerdeck.card_list)):
                if player.playerdeck.card_list[a].type is HotSprings:
                    player_count += 1
            if player_count < bather_count:
                player.bather_bonus = 0
                player.score -= 3

def chatterbox_bonus_check(current_player):
    count = 0
    for a in range(len(current_player.playerdeck.card_list)):
        if current_player.playerdeck.card_list[a].type is Encounter:
            count += 1
    if count > chatterbox_count:
        chatterbox_count = count
    for player in player_list:
        if player.chatterbox_bonus = 0
            player_count = 0
            for a in range(len(player.playerdeck.card_list)):
                if player.playerdeck.card_list[a].type is Encounter:
                    player_count += 1
            if player_count == chatterbox_count:
                player.chatterbox_bonus = 1
                player.score += 3
        elif player.chatterbox_bonus == 1:
            player_count = 0
            for a in range(len(player.playerdeck.card_list)):
                if player.playerdeck.card_list[a].type is Encounter:
                    player_count += 1
            if player_count < chatterbox_count:
                player.chatterbox_bonus = 0
                player.score -= 3

def collector_bonus_check(current_player):
    count = 0
    for a in range(len(current_player.playerdeck.card_list)):
        if current_player.playerdeck.card_list[a].type is Souvenir:
            count += 1
    if count > collector_count:
        collector_count = count
    for player in player_list:
        if player.collector_bonus = 0
            player_count = 0
            for a in range(len(player.playerdeck.card_list)):
                if player.playerdeck.card_list[a].type is Souvenir:
                    player_count += 1
            if player_count == collector_count:
                player.collector_bonus = 1
                player.score += 3
        elif player.collector_bonus == 1:
            player_count = 0
            for a in range(len(player.playerdeck.card_list)):
                if player.playerdeck.card_list[a].type is Souvenir:
                    player_count += 1
            if player_count < collector_count:
                player.collector_bonus = 0
                player.score -= 3

def gourmet_bonus_check(current_player):
    count = 0
    for a in range(len(current_player.playerdeck.card_list)):
        if current_player.playerdeck.card_list[a].type is Meal:
            count += current_player.playerdeck.card_list[a].cost
    if count > gourmet_count:
        gourmet_count = count
    for player in player_list:
        if player.gourmet_bonus = 0
            player_count = 0
            for a in range(len(player.playerdeck.card_list)):
                if player.playerdeck.card_list[a].type is Meal:
                    player_count += 1
            if player_count == gourmet_count:
                player.gourmet_bonus = 1
                player.score += 3
        elif player.gourmet_bonus == 1:
            player_count = 0
            for a in range(len(player.playerdeck.card_list)):
                if player.playerdeck.card_list[a].type is Meal:
                    player_count += 1
            if player_count < gourmet_count:
                player.gourmet_bonus = 0
                player.score -= 3

def temple_bonus_check(current_player):
    if current_player.donation > temple_bonus_first:
        temple_bonus_third = temple_bonus_second
        temple_bonus_second = temple_bonus_first
        temple_bonus_first = donation
    elif current_player.donation > temple_bonus_second:
        temple_bonus_third = temple_bonus_second
        temple_bonus_second = donation
    elif current_player.donation > temple_bonus_third:
        temple_bonus_third = donation

    for player in player_list:
        if player.temple_bonus == 0:
            if player.donation == temple_bonus_first:
                player.temple_bonus = 10
                player.score += 10
            elif player.donation == temple_bonus_second:
                player.temple_bonus = 7
                player.score += 7
            elif player.donation == temple_bonus_third:
                player.temple_bonus = 3
                player.score += 3
        elif player.temple_bonus == 10:
            if player.donation == temple_bonus_first:
                pass
            elif player.donation == temple_bonus_second:
                player.temple_bonus = 7
                player.score -= 3
            elif player.donation == temple_bonus_third:
                player.temple_bonus = 3
                player.score -= 7
            else:
                player.temple_bonus = 0
                player.score -= 10
        elif player.temple_bonus == 7:
            if player.donation == temple_bonus_first:
                player.temple_bonus = 10
                player.score += 3
            elif player.donation == temple_bonus_second:
                pass
            elif player.donation == temple_bonus_third:
                player.temple_bonus = 3
                player.score -= 4
            else:
                player.temple_bonus = 0
                player.score -= 7
        elif player.temple_bonus == 3:
            if player.donation == temple_bonus_first:
                player.temple_bonus = 10
                player.score += 7
            elif player.donation == temple_bonus_second:
                player.temple_bonus = 7
                player.score += 4
            elif player.donation == temple_bonus_third:
                pass
            else:
                player.temple_bonus = 0
                player.score -= 3
