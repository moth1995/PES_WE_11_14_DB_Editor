from .stat import Stat

class Abilities:
    def __init__(self, player):
        self.attack = Stat(player, 7, 0, 0x7F, "Attack")
        self.defence = Stat(player, 8, 0, 0x7F, "Defense")
        self.balance = Stat(player, 9, 0, 0x7F, "Balance")
        self.stamina = Stat(player, 10, 0, 0x7F, "Stamina")
        self.speed = Stat(player, 11, 0, 0x7F, "Speed")
        self.accel = Stat(player, 12, 0, 0x7F, "Accel")
        self.response = Stat(player, 13, 0, 0x7F, "Response")
        self.agility = Stat(player, 14, 0, 0x7F, "Agility")
        self.dribAcc = Stat(player, 15, 0, 0x7F, "Drib Acc")
        self.dribSpe = Stat(player, 16, 0, 0x7F, "Drib Spe")
        self.sPassAcc = Stat(player, 17, 0, 0x7F, "S Pass Acc")
        self.sPassSpe = Stat(player, 18, 0, 0x7F, "S Pass Spe")
        self.lPassAcc = Stat(player, 19, 0, 0x7F, "L Pass Acc")
        self.lPassSpe = Stat(player, 20, 0, 0x7F, "L Pass Spe")
        self.shotAcc = Stat(player, 21, 0, 0x7F, "Shot Acc")
        self.shotPow = Stat(player, 22, 0, 0x7F, "Shot Power")
        self.shotTec = Stat(player, 23, 0, 0x7F, "Shot Tech")
        self.fk = Stat(player, 24, 0, 0x7F, "FK Acc")
        self.curling = Stat(player, 25, 0, 0x7F, "Swerve")
        self.heading = Stat(player, 26, 0, 0x7F, "Heading")
        self.jump = Stat(player, 27, 0, 0x7F, "Jump")
        self.tech = Stat(player, 29, 0, 0x7F, "Tech")
        self.aggress = Stat(player, 30, 0, 0x7F, "Aggression")
        self.mental = Stat(player, 31, 0, 0x7F, "Mentality")
        self.gkAbil = Stat(player, 32, 0, 0x7F, "GK")
        self.team = Stat(player, 28, 0, 0x7F, "Team Work")

    def __iter__(self):
        return iter(
            [
                self.attack,
                self.defence,
                self.balance,
                self.stamina,
                self.speed,
                self.accel,
                self.response,
                self.agility,
                self.dribAcc,
                self.dribSpe,
                self.sPassAcc,
                self.sPassSpe,
                self.lPassAcc,
                self.lPassSpe,
                self.shotAcc,
                self.shotPow,
                self.shotTec,
                self.fk,
                self.curling,
                self.heading,
                self.jump,
                self.tech,
                self.aggress,
                self.mental,
                self.gkAbil,
                self.team,
            ]
        )
    
    def __call__(self):
        return [ability() for ability in self.__iter__()]