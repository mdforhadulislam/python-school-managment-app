from lib.data import Data
from lib.utilities import generate_id

data = Data()


class Student_Registration:
    def __init__(self):
        self.name = "Student Registration"

    def add(self):
        first_name = input("Enter Your first name**: ")
        last_name = input("Enter Your Last Name**: ")
        class_name = input("Enter Your Class Number**: ")
        roll_no = input("Enter Your Roll Number**: ")
        phone = input("Enter Your Phone Number**: ")
        address = input("Enter Your Address: ")
        email = input("Enter Your Email Address**: ")
        password = input("Enter Your Password**: ")

        if first_name and last_name and phone and class_name and password:

            id_number = generate_id(first_name, last_name)

            student_data = {
                "id": id_number,
                "first_name": first_name,
                "last_name": last_name,
                "class": class_name,
                "roll": roll_no,
                "phone": phone,
                "address": address,
                "email": email,
                "password": password,
                "payments": [],
                "attendance": []
            }
            data.create(f'.data/students-data/{id_number}.json', student_data)
            return '\nStudent Registration Successful\n' + 'Student ID Number is: ' + id_number + '\n' + 'calect Student ID Number and Password'
        else:
            return 'Student Registration Failed'

    def read(self, student_id):
        # student_id = input("Enter Your ID Number**: ")
        if student_id:
            return data.read(f'.data/students-data/{student_id}.json')
        else:
            return "Student Not Registered"

    def update(self, student_id):

        if not student_id:
            return
        student_data = data.read(f'.data/students-data/{student_id}.json')
        if type(student_data) != dict:
            return "Student Not Registered"
        first_name = input("Enter Your first name**: ")
        last_name = input("Enter Your Last Name**: ")
        class_name = input("Enter Your Class Number**: ")
        roll_no = input("Enter Your Roll Number**: ")
        phone = input("Enter Your Phone Number**: ")
        address = input("Enter Your Address: ")
        email = input("Enter Your Email Address**: ")

        update_data = {
            "first_name": first_name if first_name else student_data["first_name"],
            "last_name": last_name if last_name else student_data["last_name"],
            "class": class_name if class_name else student_data["class"],
            "roll": roll_no if roll_no else student_data["roll"],
            "phone": phone if phone else student_data["phone"],
        }
        if address:
            update_data["phone"] = address
        else:
            update_data["address"] = student_data["address"]

        update_data["email"] = email if email else student_data["email"]
        data.update(f'.data/students-data/{student_id}.json', update_data)
        return update_data

    def delete(self, student_id):

        if student_id:
            data.delete(f'.data/students-data/{student_id}.json')
            return "Student Data Deleted"
        else:
            return "Student Not Registered"
