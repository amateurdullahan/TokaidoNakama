
class Achievements():
        def __init__(self, pano_paddy_bonus="", pano_mt_bonus="", pano_sea_bonus="", gourmet_sum=0, bather_count=0, chatterbox_count=0, collector_count=0, temple_bonus_first=1, temple_bonus_second=1, temple_bonus_third=1):
            """initializing the players"""
            self.pano_paddy_bonus = pano_paddy_bonus
            self.pano_mt_bonus = pano_mt_bonus
            self.pano_sea_bonus = pano_sea_bonus
            self.gourmet_sum = gourmet_sum
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
        def gourmet_sum(self):
            """comment"""
            return self.__gourmet_sum

        @gourmet_sum.setter
        def gourmet_sum(self, value):
            """comment"""
            self.__gourmet_sum = value

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

def pano_paddy_check(Player):
    if pano_paddy_bonus == None
        if Player.pano_paddy == 3
            pano_paddy_bonus = Player.color
            Player.score += 3
