from .stat import Stat


class Position:
    def __init__(self, player):
        self.favourite_side = Stat(player, 34, 6, 0x3, "Favorite Side")
        self.registered_position = Stat(player, 6, 4, 0xF, "Registered Position")
        self.GK = Stat(player, 7, 7, 1, "GK")
        self.CWP = Stat(player, 8, 7, 1, "SW")
        self.CBT = Stat(player, 9, 7, 1, "CB")
        self.SB = Stat(player, 10, 7, 1, "SB")
        self.DM = Stat(player, 11, 7, 1, "DMF")
        self.WB = Stat(player, 12, 7, 1, "WB")
        self.CM = Stat(player, 13, 7, 1, "CMF")
        self.SM = Stat(player, 14, 7, 1, "SMF")
        self.AM = Stat(player, 15, 7, 1, "AMF")
        self.WG = Stat(player, 16, 7, 1, "WF")
        self.SS = Stat(player, 17, 7, 1, "SS")
        self.CF = Stat(player, 18, 7, 1, "CF")

    def __iter__(self):
        return iter(
            [
                self.favourite_side,
                self.registered_position,
                self.GK,
                self.CWP,
                self.CBT,
                self.SB,
                self.DM,
                self.WB,
                self.CM,
                self.SM,
                self.AM,
                self.WG,
                self.SS,
                self.CF,
            ]
        )
    
    def __call__(self):
        return [position() for position in self.__iter__()]