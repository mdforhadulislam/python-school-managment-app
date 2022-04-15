from lib.data import Data
from lib.utilities import token

data = Data()


class Student_Payments:
    def __init__(self):
        self.name = "Student Payments"
        self.month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    def create(self):
        student_id = input("Enter student id: ")
        if student_id:
            student_data = data.read('.data/students-data/' + student_id + '.json')
            if type(student_data) == dict:
                student_payment = student_data['payments']

                payment_date = input("Enter payment date format(18/08/2021): ")
                payment_month = int(input("Enter payment month Number: \n1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. July\n8. August\n9. September\n10. October\n11. November\n12. December\n"))
                is_payment = input("Is payment? (y/n): ")

                if is_payment == 'y' or is_payment == "Y":
                    is_payment = True
                if is_payment == 'n' or is_payment == "N":
                    is_payment = False

                if payment_month and payment_date:

                    payment_data = {
                        "token": token(),
                        "date": payment_date,
                        "month": self.month[payment_month - 1],
                        "is_payment": is_payment
                    }

                    student_payment.append(payment_data)

                    data.update('.data/students-data/' + student_id + '.json', student_data)

                else:
                    return "Enter valid data"
            else:
                return "Student not found"
        else:
            return "Enter student id"

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass