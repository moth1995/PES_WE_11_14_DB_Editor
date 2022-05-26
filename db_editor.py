from tkinter import Tk
from gui.gui import Gui
from pes_files import BinFile, CallnameFile
from editor.nationality import Nationality
from editor.players import Player
from csv_file import CSVFile
from editor.salary import Salary
from editor.stadiums import Stadium
from editor.team_names import TeamNames
from editor.utils.common_functions import file_read

def main():

    teams_nationality_file = BinFile("unknow_00006.ovl")
    executable_file = BinFile("SLES_556.73")
    stadiums_start_address = 3024960
    stadiums_size = 1037
    stadiums = [Stadium(executable_file, i, stadiums_start_address) for i in range(int(stadiums_size/Stadium.MAX_LEN))]

    #print(stadiums[0].name)
    #executable_file.save_file()
    nationalities_start_address = 3408
    nationalities_size = 1144
    nationalities = Nationality(
        teams_nationality_file, 
        nationalities_start_address,
        nationalities_size,
    )

    team_names_table_start_address = 13440
    team_names_table_size = 6000
    team_names_text_size = 8744

    team_names = TeamNames(
        teams_nationality_file,
        team_names_table_start_address,
        team_names_table_size,
        team_names_text_size, # tamaño en bytes desde el primer caracter de austria hasta el primero de MasterLeague Hide
    )
    
    callname_file = CallnameFile("unknow_00549.unk")
    #callname_file = CallnameFile("pes_13_unknow_00545.unk")
    #print(callname_file.callname_list[-1].name)
    #print(callname_file.callname_list[-1].file_1_id)
    #print(callname_file.callname_list[-1].afs_1_id)
    #print(callname_file.callname_list[-1].file_2_id)
    #print(callname_file.callname_list[-1].afs_2_id)
    #print(callname_file.letter_group_start_address)
    #print(callname_file.letter_group_index)
    #print(callname_file.letters)
    #callname_file.update_letters_group_index()
    #print(callname_file.letter_group_index)


    my_app = Gui()
    my_app.run()

    #print(nationalities.names)
    #print(nationalities.abbs)
    #nationalities.update_names_abbs(nationalities.names, nationalities.abbs)
    #with open('new_database_e.ovl','wb') as f:
    #    f.write(nationalities.file_bytes)

    #print(team_names.names)
    #print(team_names.abbs)
    #team_names.update_names_abbs(team_names.names, team_names.abbs)
    #print(len(teams_nationality_file.data))
    #teams_nationality_file.save_file()

    """
    db_file = file_read("unknow_00051.bin_000")
    db_size = len(db_file)
    salary_file = file_read("unknow_00051.bin_006")
    salary_size = len(salary_file)
    callnames_file = file_read("unknow_00549.unk")
    callnames_size = len(callnames_file)

    salary_data_size = 4
    salary_total = int(salary_size / salary_data_size)
    salarys = [
        Salary(
            i, 
            salary_file[
                i* salary_data_size : i * salary_data_size + salary_data_size
            ]
        ) for i in range(salary_total)
    ]

    player_data_size = 124
    players_total = int(db_size / player_data_size)
    players = [
        Player(
            i, 
            db_file[
                i* player_data_size : i * player_data_size + player_data_size
            ],
        ) for i in range(1, players_total)
    ]

    # Creamos el CSV
    csv = CSVFile("players.csv")
    csv.to_file(players)

    # Nota: todavia no se guarda nada en el archivo binario, solo en memoria, el csv es el unico que refleja los cambios hechos
    """
if __name__ == "__main__":
	main()