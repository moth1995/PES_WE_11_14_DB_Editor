from editor.utils.common_functions import file_read


class BinFile:
    HEADER_SIZE = 32
    def __init__(self, file_location):
        self.file_location = file_location
        self.data = file_read(self.file_location)
        self.header = self.data[:self.HEADER_SIZE]
        self.file_content = self.data[self.HEADER_SIZE:]
        self.size = len(self.data)

    def save_file(self):
        with open(self.file_location,'wb') as bf:
            bf.write(self.data)

    def new_save_file(self, file_location=None):
        file_location = self.file_location = file_location or self.file_location
        with open(file_location,'wb') as bf:
            bf.write(self.header)
            bf.write(self.file_content)
