from lib.data import Data

data= Data()

class StudentPayments:
    def __init__(self):
        self.name = "Student Payments"

    def create_payments(self):
        id = input("Enter student id: ")
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]

        try:
            read_student = data.read('.data/students/' + id + '.json')

            if read_student:
                payment_data = data.read('../.data/payments/' + id + '.json')

                if payment_data == "server side Error":
                    payments_date = input("Enter payments date Formet(2022-04-08): ")
                    payments_amount = int(input("Enter payments amount: "))
                    payments_month = int(input("1. January\n"+"2. February\n"+"3. March\n"+"4. April\n"+"5. May\n"+"6. June\n"+"7. July\n"+"8. August\n"+"9. September\n"+"10. October\n"+"11. November\n"+"12. December\n"+"Enter payments month number: "))
                    is_payment = input("Is this payment clear? (y/n): ")

                    if is_payment == 'y':
                        is_payment = True
                    elif is_payment == 'n':
                        is_payment = False

                    student__payments = {
                        "id": id,
                        "payments": [
                            {
                                "date": payments_date,
                                "amount": payments_amount,
                                "payment_month": month_list[payments_month-1],
                                "is_payment": is_payment
                            }
                        ]
                    }
                    data.create('../.data/payments/' + id + '.json', student__payments)
                    return  student__payments["payments"]
                else:
                    return "Student payments already exist"
            else:
                return "Student not found"
        except:
            return "Student not found"

    def read_payments(self):
        id = input("Enter student id: ")
        try:
            read_payment = data.read('../.data/payments/' + id + '.json')
            return read_payment
        except:
            return "Payment not found"


payments = StudentPayments()
print(payments.create_payments())
