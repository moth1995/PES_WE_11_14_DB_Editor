from .stat import Stat

class BasicSettings:
    def __init__(self,player):
        self.age = Stat(player, 66, 1, 0x1F, "Age")
        self.foot = Stat(player, 5, 0, 1, "Foot")
        self.injury = Stat(player, 33, 6, 0x3, "Injury Tolerance")
        self.dribble_style = Stat(player, 6, 0, 0x3, "Dribbling Style")
        self.free_kick = Stat(player, 5, 1, 0xF, "Free Kick")
        self.penalty_style = Stat(player, 5, 5, 0x7, "Penalty Kick")
        self.dropkick_style = Stat(player, 6, 2, 0x3, "Dropkick Style")
        self.goal_cel1 = Stat(player, 36, 0, 255, "Goal Celebration 1")
        self.goal_cel2 = Stat(player, 37, 0, 255, "Goal Celebration 2")
        self.growth = Stat(player, 39, 0, 0x3F, "Growth")

    def __iter__(self):
        return iter(
            [
                self.age,
                self.foot,
                self.injury,
                self.dribble_style,
                self.free_kick,
                self.penalty_style,
                self.dropkick_style,
                self.goal_cel1,
                self.goal_cel2,
                self.growth,
            ]
        )
    
    def __call__(self):
        return [basic_setting() for basic_setting in self.__iter__()]