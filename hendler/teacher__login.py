from random import Random
from lib.data import Data

data= Data()
id = Random().randint(1,10000)

class Teacher:
    def __init__(self):
        self.name="Teachers Login"

    def create_teacher(self):

        self.first_name =input("Enter your first name: ")
        self.last_name =input("Enter your last name: ")
        self.phone_number = input("Enter your phone number: ")
        self.email = input("Enter your email: ")
        self.password =input("Enter your password: ")

        if self.first_name and self.last_name and self.phone_number and self.email and self.password:
            teacherID = self.first_name + "-" + self.last_name + "-" + str(id)
            student__data = {
                "id": teacherID,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "password": self.password,
            }
            data.create('.data/teachers/' + self.first_name +"-"+ self.last_name + "-" + str(id) + ".json",student__data)
            return "Teacher Has Been Created\n" + "Your ID Number " + teacherID +"\n"+ "Clucte Your Teacher Id Number"
        else:
            return "Requested Data Problem"

    def get_teacher(self):
        id = input("Enter Your Teacher ID: ")
        if id:
            read = data.read('.data/teachers/'+id+".json")
            return read

    def update_teacher(self):
        id = input("Enter Your Student ID: ")
        if id:
            try:
                read = data.read('.data/teachers/'+id+".json")
                if read:
                    self.first_name = input("Enter your New first name: ")
                    self.last_name = input("Enter your New last name: ")
                    self.phone_number = input("Enter your New phone number: ")
                    self.email = input("Enter your New email: ")
                    self.password = input("Enter your New password: ")

                    teacher__data = {}

                    teacher__data["id"]=id

                    if self.first_name:
                        teacher__data["first_name"] = self.first_name
                    else:
                        teacher__data["first_name"] = read["first_name"]

                    if self.last_name:
                        teacher__data["last_name"] = self.last_name
                    else:
                        teacher__data["last_name"] = read["last_name"]

                    if self.phone_number:
                        teacher__data["phone_number"] = self.phone_number
                    else:
                        teacher__data["phone_number"] = read["phone_number"]

                    if self.password:
                        teacher__data["password"] = self.password
                    else:
                        teacher__data["password"] = read["password"]

                    if teacher__data:
                        try:
                            data.update('.data/teachers/' + id + ".json", teacher__data)
                            return "Teacher Has Been Updated"
                        except:
                            return "There Was Server side Error"
                    else:
                        return "No Data To Update"
                else:
                    return "Requested Data Problem"
            except:
                return "Teacher Not Found"
        else:
            return "Server Side Problem"

    def delete_teacher(self):
        id = input("Enter Your Teacher ID: ")
        if id:
            try:
                data.delete('.data/teachers/' + id + ".json")
                return "Teacher Has Been Deleted"
            except:
                return "Teacher Not Found"
        else:
            return "Server Side Problem"
