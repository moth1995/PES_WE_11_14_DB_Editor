from .stat import Stat

class SpecialAbilities:
    def __init__(self, player):
        self.dribbing = Stat(player, 21, 7, 1, "Dribbling")
        self.tactical_dribbling = Stat(player, 21, 15, 1, "Tactical Drib")
        self.positioning = Stat(player, 23, 7, 1, "Positioning")
        self.reaction = Stat(player, 23, 15, 1, "Reaction")
        self.playermaking = Stat(player, 25, 7, 1, "Playmaking")
        self.passing = Stat(player, 25, 15, 1, "Passing")
        self.scoring = Stat(player, 27, 7, 1, "Scoring")
        self.one_on_one_scoring = Stat(player, 27, 15, 1, "1-1 Scoring")
        self.post = Stat(player, 29, 7, 1, "Post")
        self.line = Stat(player, 29, 15, 1, "Line Position")
        self.middle_shooting = Stat(player, 31, 7, 1, "Mid shooting")
        self.side = Stat(player, 31, 15, 1, "Side")
        self.center = Stat(player, 19, 15, 1, "Centre")
        self.penalties = Stat(player, 19, 7, 1, "Penalties")
        self.one_touch_pass = Stat(player, 35, 0, 1, "1-T Pass")
        self.outside = Stat(player, 35, 1, 1, "Outside")
        self.marking = Stat(player, 35, 2, 1, "Marking")
        self.sliding = Stat(player, 35, 3, 1, "Sliding") 
        self.covering = Stat(player, 35, 4, 1, "Cover")
        self.d_line_control = Stat(player, 35, 5, 1, "D-L Control")
        self.penalty_gk = Stat(player, 35, 6, 1, "Penalty GK")
        self.one_on_one_gk = Stat(player, 35, 7, 1, "1-on-1 GK")
        self.long_throw = Stat(player, 37, 7, 1, "Long Throw")

    def __iter__(self):
        return iter(
            [
                self.dribbing,
                self.tactical_dribbling,
                self.positioning,
                self.reaction,
                self.playermaking,
                self.passing,
                self.scoring,
                self.one_on_one_scoring,
                self.post,
                self.line,
                self.middle_shooting,
                self.side,
                self.center,
                self.penalties,
                self.one_touch_pass,
                self.outside,
                self.marking,
                self.sliding,
                self.covering,
                self.d_line_control,
                self.penalty_gk,
                self.one_on_one_gk,
                self.long_throw,
            ]
        )
    
    def __call__(self):
        return [special_ability() for special_ability in self.__iter__()]