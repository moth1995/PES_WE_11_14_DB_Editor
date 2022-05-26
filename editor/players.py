from .appearance import Appearance
from .player_nationality import PlayerNationality
from .positions import Position
from .basic_settings import BasicSettings
from .player_callname import PlayerCallname
from .special_abilities import SpecialAbilities
from .salary import Salary
from .abilities import Abilities

class Player:
    name_encoding = "utf-16-le"
    shirt_encoding = "utf-8"
    size = 124
    max_name_size = 15
    name_bytes_length = 32
    shirt_name_bytes_length = 16

    def __init__(self, idx: int, player_bytes: bytearray):
        self.idx = idx
        self.player_bytes = player_bytes
        self.callname = PlayerCallname(self)
        self.basic_settings = BasicSettings(self)
        self.position = Position(self)
        self.nationality = PlayerNationality(self)
        self.appearance = Appearance(self)
        self.abilities = Abilities(self)
        self.special_abilities = SpecialAbilities(self)

        self.set_name_from_bytes()
        self.set_shirt_name_from_bytes()

    def set_name_from_bytes(self):
        """
        Set player name from relevant OF data bytes.
        """
        name = "???"

        all_name_bytes = self.player_bytes[: self.name_bytes_length]
        try:
            name = all_name_bytes.decode('utf-16-le').encode('utf-8').partition(b"\0")[0].decode('utf-8')
        except:
            name = f"Error (ID: {self.idx})"

        if not name:
            name = f"Unknown (ID: {self.idx})"

        self.__name = name

    @property
    def name(self):
        """
        Return player name.
        """
        return self.__name

    @name.setter
    def name(self, name:str):
        """
        Update player name with the supplied value.
        """
        new_name = name[: self.max_name_size]

        player_name_bytes = [0] * self.name_bytes_length
        new_name_bytes = str.encode(new_name, self.name_encoding)
        player_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(player_name_bytes):
            self.player_bytes[i] = byte

        self.__name = new_name

    def set_shirt_name_from_bytes(self):
        """
        Set player shirt name from relevant OF data bytes.
        """
        shirt_name_address = 32
        name_byte_array = self.player_bytes[
            shirt_name_address : shirt_name_address
            + self.shirt_name_bytes_length
        ]

        self.__shirt_name = name_byte_array.partition(b"\0")[0].decode(self.shirt_encoding)

    @property
    def shirt_name(self):
        """
        Return player shirt name.
        """
        return self.__shirt_name

    @shirt_name.setter
    def shirt_name(self, shirt_name:str):
        shirt_name_address = 32
        new_name = shirt_name[: self.max_name_size].upper()

        player_shirt_name_bytes = [0] * self.shirt_name_bytes_length
        new_name_bytes = str.encode(new_name)
        player_shirt_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(player_shirt_name_bytes):
            self.player_bytes[shirt_name_address + i] = byte

        self.__shirt_name = new_name

    def __iter__(self):
        return iter(
            [
                self.idx, 
                self.name, 
                self.shirt_name,
                self.callname,
            ]
        )
