from random import Random

from lib.data import Data

data = Data()
id = Random().randint(1, 10000)


class Student:
    def __init__(self):
        self.name = "Student Login"

    def create_student(self):

        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.class_name = input("Enter your class: ")
        self.present_address = input("Enter your present address: ")
        self.permanent_address = input("Enter your permanent address: ")
        self.phone_number = input("Enter your phone number: ")
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")

        if self.first_name and self.last_name and self.phone_number and self.class_name and self.email and self.password:
            studentID = self.first_name + "-" + self.last_name + "-" + str(id)
            student__data = {
                "id": studentID,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "class_name": self.class_name,
                "present_address": self.present_address,
                "permanent_address": self.permanent_address,
                "email": self.email,
                "password": self.password,
            }
            data.create('.data/students/' + self.first_name + "-" +
                        self.last_name + "-" + str(id) + ".json", student__data)
            return "\nStudent Has Been Created\n" + "Your ID Number " + studentID + "\n" + "Clucte your studentID Number"
        else:
            return "Requested Data Problem"

    def get_student(self):
        id = input("Enter Your Student ID: ")
        if id:
            read = data.read('.data/students/'+id+".json")
            return read

    def update_student(self):
        id = input("Enter Your Student ID: ")
        if id:
            try:
                read = data.read('.data/students/'+id+".json")
                if read:
                    self.first_name = input("Enter your New first name: ")
                    self.last_name = input("Enter your New last name: ")
                    self.class_name = input("Enter your New class: ")
                    self.present_address = input(
                        "Enter your New present address: ")
                    self.permanent_address = input(
                        "Enter your New permanent address: ")
                    self.phone_number = input("Enter your New phone number: ")
                    self.email = input("Enter your New email: ")
                    self.password = input("Enter your New password: ")

                    student__data = {}

                    student__data["id"] = id

                    if self.first_name:
                        student__data["first_name"] = self.first_name
                    else:
                        student__data["first_name"] = read["first_name"]

                    if self.last_name:
                        student__data["last_name"] = self.last_name
                    else:
                        student__data["last_name"] = read["last_name"]

                    if self.class_name:
                        student__data["class_name"] = self.class_name
                    else:
                        student__data["class_name"] = read["class_name"]

                    if self.present_address:
                        student__data["present_address"] = self.present_address
                    else:
                        student__data["present_address"] = read["present_address"]

                    if self.permanent_address:
                        student__data["permanent_address"] = self.permanent_address
                    else:
                        student__data["permanent_address"] = read["permanent_address"]

                    if self.phone_number:
                        student__data["phone_number"] = self.phone_number
                    else:
                        student__data["phone_number"] = read["phone_number"]

                    if self.password:
                        student__data["password"] = self.password
                    else:
                        student__data["password"] = read["password"]

                    if student__data:
                        try:
                            data.update('.data/students/' + id +
                                        ".json", student__data)
                            return "Student Has Been Updated"
                        except:
                            return "There Was Server side Error"
                    else:
                        return "No Data To Update"
                else:
                    return "Requested Data Problem"
            except:
                return "Student Not Found"
        else:
            return "Server Side Problem"

    def delete_student(self):
        id = input("Enter Your Student ID: ")
        if id:
            try:
                read = data.read('.data/students/'+id+".json")
                if read == "server side Error":
                    return "Student Not Found"
                else:
                    data.delete('.data/students/' + id + ".json")
                    return "Student Has Been Deleted"
            except:
                return "Student Not Found"
        else:
            return "Server Side Problem"
