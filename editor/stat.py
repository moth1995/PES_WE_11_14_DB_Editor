from .utils.common_functions import zero_fill_right_shift


class Stat:
    def __init__(self, player, offset:int, shift:int, mask:int, name:str):
        self.player = player
        self.offset = offset + 48 
        self.shift = shift
        self.mask = mask
        self.name = name

    def get_value(self):
        j = (self.player.player_bytes[self.offset]) << 8 | (self.player.player_bytes[(self.offset - 1)])
        j = zero_fill_right_shift(j,self.shift)
        j &= self.mask
        return j

    def set_value(self, new_value:int):
        j = (self.player.player_bytes[self.offset]) << 8 | (self.player.player_bytes[(self.offset - 1)])
        k = 0xFFFF & (self.mask << self.shift ^ 0xFFFFFFFF)
        j &= k
        new_value &= self.mask
        new_value <<= self.shift
        new_value = j | new_value
        self.player.player_bytes[(self.offset - 1)] = (new_value & 0xFF)
        self.player.player_bytes[self.offset] = (zero_fill_right_shift(new_value,8))

    def __call__(self):
        return self.get_value()
