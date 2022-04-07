import math
from random import Random

from lib.data import Data

data= Data()
id = Random().randint(1,10000)

class Student:
    def __init__(self):
        self.name="f"

    def create_student(self):
        self.first_name = str(input("Enter your first name: "))
        self.last_name = str(input("Enter your last name: "))
        self.age = int(input("Enter your age: "))
        self.class_name = str(input("Enter your class: "))
        self.present_address = str(input("Enter your present address: "))
        self.permanent_address = str(input("Enter your permanent address: "))
        self.phone_number = str(input("Enter your phone number: "))
        self.email = str(input("Enter your email: "))
        self.password = str(input("Enter your password: "))

