from .utils.common_functions import to_b_int32, to_int

class TeamNames:

    def __init__(self, file_bytes:bytearray, table_start_address:int, table_size:int, text_size):
        self.file_bytes = file_bytes.data
        self.table_start_address = table_start_address
        self.table_size = table_size
        self.table_bytes = self.file_bytes[self.table_start_address : self.table_start_address + self.table_size]
        self.base_address = to_int(self.file_bytes[8:12])
        self.set_offset_tables_from_bytes()
        self.text_lenght = text_size
        self.middle_chunk = self.file_bytes[self.name_offset_table[0] + self.text_lenght : self.table_start_address]
        self.end_chunk = self.file_bytes[self.table_start_address + self.table_size : ]
        self.set_names()
        self.set_abbs()

    def set_offset_tables_from_bytes(self):
        self.name_offset_table = []
        self.abb_offset_table = []

        for i in range(0, self.table_size, 16):
            self.name_offset_table.append(to_int(self.table_bytes[i : i + 4]) - self.base_address)
            self.abb_offset_table.append(to_int(self.table_bytes[i + 4 : i + 8]) - self.base_address)

    def get_name_by_id(self,idx:int):
        return self.file_bytes[self.name_offset_table[idx]:].partition(b"\0")[0].decode('utf-8')

    def get_abb_by_id(self,idx:int):
        return self.file_bytes[self.abb_offset_table[idx]:].partition(b"\0")[0].decode('utf-8')

    def set_names(self):
        names = [self.get_name_by_id(i) for i in range(len(self.name_offset_table))]
        self.__names = names

    @property
    def names(self):
        return self.__names

    def set_abbs(self):
        abbs = [self.get_abb_by_id(i) for i in range(len(self.abb_offset_table))]
        self.__abbs = abbs
    
    @property
    def abbs(self):
        return self.__abbs

    def update_names_abbs(self, new_names:list, new_abbs:list):
        if (len(self.names) != len(new_names)) or (len(self.abbs) != len(new_abbs)):
            raise ValueError("Different lenght of list")
        new_names_abbs_bytes = b''
        new_offsets_table_bytes = b''
        count = self.base_address + self.name_offset_table[0]
        for i in range(len(self.name_offset_table)):
            new_offsets_table_bytes+=to_b_int32(count)
            new_name_bytes = new_names[i].encode('utf-8') + bytearray(1)
            new_names_abbs_bytes+=new_name_bytes
            count+=len(new_name_bytes)
            new_offsets_table_bytes+=to_b_int32(count)
            new_abbs_bytes = new_abbs[i].encode('utf-8') + bytearray(1)
            count+=len(new_abbs_bytes)
            new_names_abbs_bytes+=new_abbs_bytes
        # filling the end of the chunk with zeros
        free_space = self.text_lenght - len(new_names_abbs_bytes)
        if free_space<0:
            raise ValueError("There's not enough space in the file")
        new_names_abbs_bytes+=bytearray(free_space)
        new_offsets_table_bytes = bytearray(new_offsets_table_bytes)
        new_table_bytes = self.table_bytes
        j = 0
        for i in range(0,self.table_size,16):
            new_table_bytes[i : i + 4] = new_offsets_table_bytes[j : j + 4]
            new_table_bytes[i + 4 : i + 8] = new_offsets_table_bytes[j + 4 : j + 8]
            j+=8


        team_names_chunk = new_names_abbs_bytes + self.middle_chunk + new_table_bytes + self.end_chunk
        #bin_file.data[self.name_offset_table[0] :] = bytearray(team_names_chunk)
        #bin_file.data[self.table_start_address : self.table_start_address + self.table_size] = bytearray(new_offsets_table_bytes)
        
        self.file_bytes[self.name_offset_table[0] :] = bytearray(team_names_chunk)
        #self.file_bytes[self.table_start_address : self.table_start_address + self.table_size] = bytearray(new_offsets_table_bytes)
        self.table_bytes = bytearray(new_table_bytes)
        self.set_offset_tables_from_bytes()
        self.set_names()
        self.set_abbs()
