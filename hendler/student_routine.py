from lib.data import Data

data = Data()


class Student_Routine:
    def __init__(self):
        self.name = "Student Routine"
        self.day = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

    def add(self):
        class_name = input("Enter Class: ")
        if class_name:
            routine_data = data.read('.data/class-routine/' + class_name + '.json')
            if type(routine_data) == dict:
                return "This Class Routine Already Exist"
            else:
                routine = {'class': class_name, 'routine': []}
                for day in range(0, 6):
                    class_period = int(input(f"\nEnter {self.day[day]} Class period: "))
                    single_day_routine = []
                    for period in range(1, class_period + 1):
                        single_period = {}
                        print(f'\n {period} Period:')
                        subject_name = input("Enter Subject Name: ")
                        starting_time = input("Enter Starting Time: ")
                        ending_time = input("Enter Ending Time: ")
                        teacher_name = input("Enter Teacher Name: ")

                        single_period["subject"] = subject_name
                        single_period["starting_time"] = starting_time
                        single_period["ending_time"] = ending_time
                        single_period["teacher"] = teacher_name

                        single_day_routine.append(single_period)
                        day_routine = {
                            self.day[day]: single_day_routine
                        }
                    routine['routine'].append(day_routine)
                data.create('../.data/class-routine/' + class_name + '.json', routine)
                return "Class Routine Added Successfully"
        else:
            return "Enter Class"

    def read(self):
        class_name = input("Enter Class: ")
        if class_name:
            read_routine = data.read('../.data/class-routine/'+class_name+".json")
            if type(read_routine) == dict:
                for days in read_routine['routine']:
                    for dayname in self.day:
                        try:
                            for subject in days[dayname]:
                                # print(subject)
                                print(f'day Name:{dayname}  subject Name:{subject["subject"]}  teacher Name:{subject["teacher"]}  class Start Time:{subject["starting_time"]}  class End Time:{subject["ending_time"]}')
                        except KeyError:
                            pass

            else:
                return "Routine Not Found"
        else:
            return "Enter Class"

    def update(self):
        pass

    def delete(self):
        class_name = input("Enter Class: ")
        if class_name:
            routine_data = data.read('../.data/class-routine/'+class_name+'.json')
            if type(routine_data) == dict:
                data.delete('../.data/class-routine/'+class_name+'.json')
                return "Routine Deleted"
            else:
                return "Routine Not Found"
        else:
            return "Enter Class"
