from lib.data import Data
from lib.utilities import list_files

data = Data()


def all_student_red():
    file_lists = list_files('.data/students-data')
    for file_name in file_lists:
        student_data = data.read(f'.data/students-data/{file_name}')
        print(f'\nID: {student_data["id"]}')
        print(f'    Name: {student_data["first_name"]} {student_data["last_name"]}')
        print(f'    Class: {student_data["class"]}')
        print(f'    Roll: {student_data["roll"]}')
        print(f'    Phone: {student_data["phone"]}')
        print(f'    Address: {student_data["address"]}')
        print(f'    E-mail: {student_data["email"]}')
    return ""
