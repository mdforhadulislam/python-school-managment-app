from lib.data import Data
from lib.utilities import token

data = Data()
token = token()


class Teacher_Payments:
    def __init__(self):
        self.name = "Teacher Payments"
        self.month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    def add(self):
        if not (teacher_id := input("Enter Teacher Id: ")):
            return "Enter Teacher id"
        teacher_data = data.read(f'.data/teachers-data/{teacher_id}.json')
        if type(teacher_data) != dict:
            return "Teacher not found"
        teacher_payment = teacher_data['payments']

        payment_date = input("Enter payment date format(18/08/2021): ")
        payment_amount = int(input("Enter payment amount: "))
        payment_month = int(input("Enter payment month Number: \n1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. July\n8. August\n9. September\n10. October\n11. November\n12. December\n"))
        is_payment = input("Is payment? (y/n): ")

        if is_payment in ['y', "Y"]:
            is_payment = True
        if is_payment in ['n', "N"]:
            is_payment = False

        if payment_month and payment_date:

            payment_data = {
                "token": token,
                "date": payment_date,
                "amount": payment_amount,
                "month": self.month[payment_month - 1],
                "is_payment": is_payment
            }

            teacher_payment.append(payment_data)

            data.update(f'.data/teachers-data/{teacher_id}.json', teacher_data)
            return "\nPayment Successfully Added\n" + 'Token ID Number is: ' + str(token) + '\n' + 'calect Token ID Number'
        else:
            return "Enter valid data"

    def read(self, teacher_id):
        # teacher_id = input("Enter Teacher Id: ")
        if not teacher_id:
            return "Enter Teacher id"
        teacher_data = data.read(f'.data/teachers-data/{teacher_id}.json')
        if type(teacher_data) != dict:
            return "Teacher Not Registered"
        teacher_payment = teacher_data['payments']
        for payment in teacher_payment:
            if payment['is_payment'] == True:
                clear_payment = "Paid"
            elif payment['is_payment'] == False:
                clear_payment = "Due"   
            print(f'payment date: {payment["date"]} payment amount: {payment["amount"]} payment month: {payment["month"]} is payment: {clear_payment}')

    def update(self, teacher_id):
        # teacher_id = input("Enter Teacher Id: ")
        if not teacher_id:
            return "Enter student id"
        teacher_data = data.read(f'.data/teachers-data/{teacher_id}.json')

        if type(teacher_data) != dict:
            return "Teacher Not Registered"
        token_id = int(input("Enter token id: "))
        teacher_payment = teacher_data['payments']

        for payment in teacher_payment:
            if int(payment['token']) == token_id:
                find_token = payment

                payment_date = input("Enter payment date format(18/08/2021): ")
                payment_amount = input("Enter payment amount: ")
                payment_month = input("Enter payment month Number: \n1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. July\n8. August\n9. September\n10. October\n11. November\n12. December\n")
                is_payment = input("Is payment? (y/n): ")

                if is_payment == 'n':
                    is_payments = False

                elif is_payment == 'y':
                    is_payments = True
                find_token['date'] = payment_date if payment_date else find_token['date']
                find_token['month'] = (
                    self.month[int(payment_month) - 1]
                    if payment_month
                    else find_token['month']
                )
                if payment_amount:
                    find_token['amount'] = payment_amount
                else:
                    find_token['amount'] = find_token['amount']

                if is_payment:
                    find_token['is_payment'] = is_payments
                else:
                    find_token['is_payment'] = find_token['is_payment']

                data.update(f'.data/teachers-data/{teacher_id}.json', teacher_data)
                return "Data Updated"

    def delete(self, teacher_id):
        # teacher_id = input("Enter Teacher Id: ")
        if not teacher_id:
            return "Enter student id"
        teacher_data = data.read(f'.data/teachers-data/{teacher_id}.json')
        if type(teacher_id) != dict:
            return "Teacher Not Registered"
        token_id = int(input("Enter token id: "))
        teacher_payment = teacher_data['payments']

        for payment in teacher_payment:
            if int(payment['token']) == token_id:
                teacher_payment.remove(payment)
                data.update(f'.data/teachers-data/{teacher_id}.json', teacher_data)
                return "Payment Data Deleted"
