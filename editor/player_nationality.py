from .stat import Stat

class PlayerNationality:
    def __init__(self, player):
        self.nationality = Stat(player, 65, 0, 0xFF, "Nationality")

    def __iter__(self):
        return iter(
            [
                self.nationality,
            ]
        )
    
    def __call__(self):
        return [nationality() for nationality in self.__iter__()]
