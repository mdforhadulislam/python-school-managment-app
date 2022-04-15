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
            data.create('.data/students-data/' + id_number + '.json', student_data)
            return '\nStudent Registration Successful\n' + 'Student ID Number is: ' + id_number + '\n' + 'calect Student ID Number and Password'
        else:
            return 'Student Registration Failed'

    def update(self):
        student_id = input("Enter Your ID Number**: ")
        if student_id:
            student_data = data.read('.data/students-data/' + student_id + '.json')
            if type(student_data) == dict:
                first_name = input("Enter Your first name**: ")
                last_name = input("Enter Your Last Name**: ")
                class_name = input("Enter Your Class Number**: ")
                roll_no = input("Enter Your Roll Number**: ")
                phone = input("Enter Your Phone Number**: ")
                address = input("Enter Your Address: ")
                email = input("Enter Your Email Address**: ")

                update_data = {}
                if first_name:
                    update_data["first_name"] = first_name
                else:
                    update_data["first_name"] = student_data["first_name"]

                if last_name:
                    update_data["last_name"] = last_name
                else:
                    update_data["last_name"] = student_data["last_name"]

                if class_name:
                    update_data["class"] = class_name
                else:
                    update_data["class"] = student_data["class"]

                if roll_no:
                    update_data["roll"] = roll_no
                else:
                    update_data["roll"] = student_data["roll"]

                if phone:
                    update_data["phone"] = phone
                else:
                    update_data["phone"] = student_data["phone"]

                if address:
                    update_data["phone"] = address
                else:
                    update_data["address"] = student_data["address"]

                if email:
                    update_data["email"] = email
                else:
                    update_data["email"] = student_data["email"]

                data.update('.data/students-data/' + student_id + '.json', update_data)
                return update_data

            else:
                return "Student Not Registered"

    def read(self):
        student_id = input("Enter Your ID Number**: ")
        if student_id:
            student_data = data.read('.data/students-data/' + student_id + '.json')
            return student_data

        else:
            return "Student Not Registered"

    def delete(self):
        student_id = input("Enter Your ID Number**: ")
        if student_id:
            data.delete('.data/students-data/' + student_id + '.json')
            return "Student Data Deleted"
        else:
            return "Student Not Registered"
