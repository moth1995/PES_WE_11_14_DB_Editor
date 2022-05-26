from editor.utils import *
from . import BinFile
from .callnames import Callname

class CallnameFile(BinFile):
    MAGIC_NUMBER = bytearray([0x01, 0x00, 0x00, 0x00])
    CALLNAME_BYTES_SIZE = 56
    CALLNAMES_START = 8
    EXTRA_ENDING_ZEROS_SIZE = 40
    
    def __init__(self, file_location):
        super(CallnameFile, self).__init__(file_location)
        self.size = to_int(self.header[4:8])
        
        self.total_callnames = to_int(self.file_content[:2])
        self.total_callnames_groups = to_int(self.file_content[2:4])
        self.extra_chunk_for_pes5_we9_le = to_int(self.file_content[4:6])
        self.total_letter_group = to_int(self.file_content[6:8])
        self.letter_group_size = self.total_letter_group * INT_16_SIZE
        self.letter_group_start_address = self.size - self.letter_group_size - self.EXTRA_ENDING_ZEROS_SIZE
        self.get_callnames_list()
        self.set_letters_index_from_bytes()
        self.set_letters_by_index()

    def get_callname_offset(self, idx:int):
        return self.CALLNAMES_START + self.CALLNAME_BYTES_SIZE * idx

    def get_callname_bytes(self, offset:int):
        return self.file_content[offset : offset + self.CALLNAME_BYTES_SIZE]

    def get_callnames_list(self):
        self.callname_list = list()
        for i in range(self.total_callnames):
            self.callname_list.append(
                Callname(
                    i,
                    self.get_callname_bytes(self.get_callname_offset(i))
                )
            )

    def fix_callnames_ids(self):
        """
        Updates the callname id after we make a alphabetical reorder
        """
        for i in range(self.total_callnames):
            self.callname_list[i].idx = i

    def order_alphabetically(self):
        """
        Function to sort alphabetically the callnames
        """
        self.callname_list = sorted(self.callname_list, key=lambda x: x.name)
        self.fix_callnames_ids()
        self.update_letters_group_index()
    
    def set_letters_index_from_bytes(self):
        """
        Initialization of letter_group list
        """
        self.letter_group_index = []
        for i in range(self.total_letter_group):
            offset = get_offset(self.letter_group_start_address, INT_16_SIZE, i)
            self.letter_group_index.append(to_int(self.file_content[ offset : offset + INT_16_SIZE]))
    
    def set_letters_by_index(self):
        self.letters = []
        for index in self.letter_group_index:
            self.letters.append(self.callname_list[index].name[0])
            
    def update_letters_group_index(self):
        self.letter_group_index = []
        for j in range(len(self.letters)):
            for i in range (len(self.callname_list)):
                if self.callname_list[i].name[0] == self.letters[j]:
                    break
            idx = self.callname_list[i].idx
            self.letter_group_index.append(idx)

    def add_callname(self, quantity_of_files):
        data = b''
        for i in range(quantity_of_files):
            base_bytes = bytearray([0] * self.CALLNAME_BYTES_SIZE)
            default_data = bytearray([0xFF,0xFF,0x02,00,0xFF,0xFF,0x02,00])
            new_name = f"CALLNAME {self.total_callnames+i}".encode("utf-8")
            base_bytes[:8] = default_data
            base_bytes[8:len(new_name)] = new_name
            data+=base_bytes
            self.total_callnames+=1
