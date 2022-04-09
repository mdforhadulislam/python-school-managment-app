from lib.data import Data

data = Data()


class TeacherPayments:
    def __init__(self):
        self.name = "Teacher Payments"

    def create_payments(self):
        id = input("Enter teacher id: ")
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]

        try:
            read_teacher = data.read('.data/teachers/' + id + '.json')

            if read_teacher:
                payment_data = data.read('../.data/teacher-payments/' + id + '.json')

                if payment_data == "server side Error":
                    payments_date = input("Enter payments date Formet(2022-04-08): ")
                    payments_amount = int(input("Enter payments amount: "))
                    payments_month = int(input("1. January\n"+"2. February\n"+"3. March\n"+"4. April\n"+"5. May\n"+"6. June\n"+"7. July\n"+"8. August\n"+"9. September\n"+"10. October\n"+"11. November\n"+"12. December\n"+"Enter payments month number: "))
                    is_payment = input("Is this payment clear? (y/n): ")

                    if is_payment == 'y':
                        is_payment = True
                    elif is_payment == 'n':
                        is_payment = False

                    teacher__payments = {
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
                    data.create('../.data/teacher-payments/' + id + '.json', teacher__payments)
                    return  teacher__payments
                else:
                    return "Teacher payments already exist"
            else:
                return "Teacher not found"
        except:
            return "Teacher not found"

    def read_payments(self):
        id = input("Enter Teacher id: ")
        if id:
            payment_data = data.read('../.data/teacher-payments/'+id+'.json')
            return payment_data
        else:
            return "Payment File Not Created"

    def update_payments(self):
        id = input("Enter Teacher id: ")
        month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                      "November", "December"]
        read_payment = data.read('../.data/teacher-payments/' + id + '.json')

        if read_payment:
            payments_date = input("Enter payments date Formet(2022-04-08): ")
            payments_amount = int(input("Enter payments amount: "))
            payments_month = int(input("1. January\n" + "2. February\n" + "3. March\n" + "4. April\n" + "5. May\n" + "6. June\n" + "7. July\n" + "8. August\n" + "9. September\n" + "10. October\n" + "11. November\n" + "12. December\n" + "Enter payments month number: "))
            is_payment = input("Is this payment clear? (y/n): ")

            if is_payment == 'y':
                is_payment = True
            elif is_payment == 'n':
                is_payment = False

            if payments_date and payments_amount and payments_month and is_payment:
                teacher__payments = {
                    "id": id,
                    "payments": []
                }
                new_payments={
                    "date":payments_date,
                    "amount":payments_amount,
                    "payment_month":month_list[payments_month-1],
                    "is_payment":is_payment
                }
                teacher__payments["payments"] = read_payment["payments"]
                teacher__payments["payments"].append(new_payments)
                data.update('../.data/payments/'+id+".json",teacher__payments)
                return "Paments update Successfull"
            else:
                return "There are problem in your request "
        else:
            return "Teacher Payment Not Found"

    def delete_payments(self):
        id = input("Enter teacher id: ")
        if id:
            value = data.read('../.data/teacher-payments/'+id+".json")
            if value == "server side Error":
                return "Payments File Not Found"
            else:
                data.delete('../.data/teacher-payments/' + id + ".json")
                return 'Payments Deleted'
        else:
            return "Teacher ID Invalide"