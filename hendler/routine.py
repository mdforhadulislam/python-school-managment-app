from lib.data import Data

data = Data()


class Routine:
    def __init__(self):
        self.name = "Routine"

    def get_routine(self):
        class_name = int(input("Enter class: "))
        if class_name:
            read = data.read('../.data/routines/' + str(class_name) + '.json')
            if read == "Server Side Error":
                return "this class Routine Not Exist"
            else:
                return read
        else:
            return "Enter class name"

    def create_routine(self):
        class_name = int(input("Enter class: "))
        day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if class_name:
            preiod = int(input("Enter period: "))
            if preiod:
                routine = []
                for number in range(1, preiod + 1):
                    day__number = int(input(
                        "1. Monday\n" + "2. Tuesday\n" + "3. Wednesday\n" + "4. Thursday\n" + "5. Friday\n" + "6. Saturday\n" + "7. Sunday\n" + "Enter day: "))
                    subject__name = input("Enter subject Name: ")
                    teached_by = input("Enter teacher Name: ")
                    if day__number and subject__name and teached_by:
                        routine.append({"day": day[day__number - 1], "subject": subject__name,"teached_by": teached_by})
                    else:
                        return "Enter all data"
                main__routine = {"class": class_name, "routine": routine}
                if main__routine:
                    read = data.read('../.data/routines/'+str(class_name)+'.json')
                    if read =="Server Side Error":
                        return "this class Routine Already Exist"
                    else:
                        data.create('../.data/routines/' + str(class_name) + '.json', main__routine)
                else:
                    return "Server Side Error"
            else:
                return "Enter period Number"
        else:
            return "Enter class name"

    def update_routine(self):
        class_name = int(input("Enter class: "))
        day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if class_name:
            read = data.read('../.data/routines/' + str(class_name) + '.json')
            if read == "Server Side Error":
                return "this class Routine Not Exist"
            else:
                day__number = int(input(
                    "1. Monday\n" + "2. Tuesday\n" + "3. Wednesday\n" + "4. Thursday\n" + "5. Friday\n" + "6. Saturday\n" + "7. Sunday\n" + "Enter day: "))
                subject__name = input("Enter subject Name: ")
                teached_by = input("Enter teacher Name: ")
                if day__number and subject__name and teached_by:
                    routine = read["routine"]
                    routine.append({"day": day[day__number - 1], "subject": subject__name, "teached_by": teached_by})
                    main__routine = {"class": class_name, "routine": routine}
                    data.update('../.data/routines/' + str(class_name) + '.json', main__routine)
                    return "Routine Updated"
                else:
                    return "Enter all data"
        else:
            return "Enter class name"

    def delete_routine(self):
        class_name = int(input("Enter class: "))
        if class_name:
            read = data.read('../.data/routines/' + str(class_name) + '.json')
            if read == "Server Side Error":
                return "this class Routine Not Exist"
            else:
                data.delete('../.data/routines/' + str(class_name) + '.json')
                return "Routine Deleted"
        else:
            return "Enter class name"

