from lib.data import Data
from lib.utilities import generate_id

data = Data()


class Teacher_Registration:
    def __init__(self):
        self.name = "Teacher Registration"

    def add(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        if first_name and last_name and email and password:

            teacher_id = generate_id(first_name, last_name)

            teacher_data = {
                "teacher_id": teacher_id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password,
                "phone": phone,
                "payments": []
            }

            data.create('.data/teachers-data/'+teacher_id+'.json', teacher_data)
            return '\nTeacher created successfully\n' + "Teacher ID: " + teacher_id + '\n' + 'calect Student ID Number and Password'
        else:
            return "Please fill all the fields"

    def read(self):
        teacher_id = input("Enter teacher ID: ")
        if teacher_id:
            teacher_data = data.read('.data/teachers-data/'+teacher_id+'.json')
            if type(teacher_data) == dict:
                return teacher_data
        else:
            return "Please enter teacher ID"

    def update(self):
        teacher_id = input("Enter teacher ID: ")
        if teacher_id:
            teacher_data = data.read('.data/teachers-data/'+teacher_id+'.json')
            if type(teacher_data) == dict:
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")

                if first_name:
                    teacher_data['first_name'] = first_name
                else:
                    teacher_data['first_name'] = teacher_data['first_name']

                if last_name:
                    teacher_data['last_name'] = last_name
                else:
                    teacher_data['last_name'] = teacher_data['last_name']

                if email:
                    teacher_data['email'] = email
                else:
                    teacher_data['email'] = teacher_data['email']

                if phone:
                    teacher_data['phone'] = phone
                else:
                    teacher_data['phone'] = teacher_data['phone']

                data.update('.data/teachers-data/'+teacher_id+'.json', teacher_data)
                return 'Teacher updated successfully'

            else:
                return "Teacher not found"
        else:
            return "Please enter teacher ID"

    def delete(self):
        teacher_id = input("Enter teacher ID: ")
        if teacher_id:
            teacher_data = data.read('.data/teachers-data/'+teacher_id+'.json')
            if type(teacher_data) == dict:
                data.delete('.data/teachers-data/'+teacher_id+'.json')
                return 'Teacher deleted successfully'
            else:
                return "Teacher not found"
        else:
            return "Please enter teacher ID"
