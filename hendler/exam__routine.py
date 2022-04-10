from lib.data import Data

data = Data()

class ExamRoutine:
    def __init__(self):
        self.name = "Exam Routine"

    def get_exam_routine(self):
        class__name = input("Enter class name: ")
        if class__name:
            class__exam__routine = data.read('../.data/exam-routines/'+class__name+'.json')
            if class__exam__routine:
                return class__exam__routine
            else:
                return "No exam routine found"
        else:
            return "Please enter class name"

    def create_exam_routine(self):
        class__name = input("Enter class name: ")
        if class__name:
            exam__subject__number = int(input("Enter exam subject number: "))
            class__exam__routine = {}
            routine = []
            if exam__subject__number:
                for number in range(1, exam__subject__number+1):
                    subject = input("Enter exam subject name: ")
                    exam__date = input("Enter exam date formed(18/08/2022): ")
                    if subject and exam__date:
                        routine.append({"subject": subject, "date": exam__date})
                    else:
                        return "Enter subject and date"
                class__exam__routine["class"] = class__name
                class__exam__routine["routine"] = routine
                data.create('../.data/exam-routines/'+class__name+'.json', class__exam__routine)
            else:
                return "Exam subject number is required"
        else:
            return "Please enter class name"

    def update_exam_routine(self):
        class__name = input("Enter class name: ")
        if class__name:
            read_exam_routine = data.read('../.data/exam-routines/'+class__name+'.json')
            if read_exam_routine:

            else:
                return "No exam routine found"
        else:
            return "Please enter class name"

    def delete_exam_routine(self):
        return



exam_routine = ExamRoutine()
print(exam_routine.get_exam_routine())