from .stat import Stat

class Appearance:
    def __init__(self, player):
        self.face = Stat(player, 55, 0, 3, "Face")
        self.face_type = Stat(player, 53, 4, 0x7FF, "Face Type")
        self.skin = Stat(player, 68, 0, 0x7, "Skin")
        self.head_length = Stat(player, 43, 4, 0xF, "Head Length")
        self.head_width = Stat(player, 44, 0, 0xF, "Head Width")
        self.hair_type = Stat(player, 45, 0, 0x7FF, "Hair")
        self.special_hairstyles_2 = Stat(player, 52, 6, 1, "Is Special Hairstyles 2")
        self.height = Stat(player, 41, 0, 0x3F, "Height")
        self.weight = Stat(player, 42, 0, 0x7F, "Weight")

    def __iter__(self):
        return iter(
            [
                self.face,
                self.face_type,
                self.skin,
                self.head_length,
                self.head_width,
                self.hair_type,
                self.special_hairstyles_2,
                self.height,
                self.weight,
            ]
        )
    
    def __call__(self):
        return [appearance() for appearance in self.__iter__()]