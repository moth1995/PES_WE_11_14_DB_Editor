class Stadium:

    MAX_LEN = 61

    def __init__(self,bin_file, idx, start_address):
        self.start_address = start_address
        self.idx = idx
        self.bin_file = bin_file
        self.get_offset()
        self.get_name()

    def get_offset(self):
        self.offset = self.start_address + self.idx * self.MAX_LEN

    def get_name(self):
        self.name = self.bin_file.data[self.offset : self.offset + self.MAX_LEN].partition(b"\0")[0].decode('utf-8',"ignore")

    def set_name(self, new_name):
        if 0 < len(new_name) < self.MAX_LEN:
            new_name = new_name[: self.MAX_LEN]
            stadium_name_bytes = [0] * self.MAX_LEN
            new_name_bytes = str.encode(new_name, "utf-8","ignore")
            stadium_name_bytes[: len(new_name_bytes)] = new_name_bytes
            for i, byte in enumerate(stadium_name_bytes):
                self.bin_file.data[self.offset + i] = byte
            self.get_name()
            return "Stadium name changed!"
        else:
            raise ValueError("Stadium name can't be empty or bigger than 60 characters")
