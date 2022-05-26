import csv

class CSVFile:
    headers = [
        "ID",
        "NAME",
        "SHIRT_NAME",
    ]
    encoding = "utf-8"

    def __init__(self, file_location):
        self.__file_location = file_location

    @property
    def file_location(self):
        return self.__file_location

    @file_location.setter
    def file_location(self, valor):
        if valor != "":
            self.__file_location = valor
        else:
            raise ValueError("CSV file location can't be empty")

    def make(self):
        """
        Creates the csv into the disk
        """
        with open(self.file_location, 'w', newline='', encoding=self.encoding) as csv_file:
            writer = csv.writer(csv_file, delimiter=',')            
            writer.writerow(self.headers)

    def to_file(self, players):
        """
        Receives a list of players, creates the csv using the method "make" and then writes the data
        """
        self.make()
        with open(self.file_location, 'a', newline='', encoding=self.encoding) as csv_file:
            writer=csv.writer(csv_file, delimiter=',')
            writer.writerows(players)

    def load(self):
        with open(self.file_location, 'r', encoding='utf-8') as csvf:
            # list to store the names of columns
            csv_reader = csv.reader(csvf, delimiter = ',')
            list_of_column_names = [] 
            print(csv_reader[0])