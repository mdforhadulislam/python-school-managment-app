import os
from lib.data import Data
from lib.utilities import list_files
import datetime
data = Data()
date = datetime.datetime.now()


class Student_Attendance:
    def __init__(self):
        self.name = "Student Attendance"
        self.student_files = list_files('../.data/students-data/')

    def add(self):
        for student in self.student_files:
            student_data = data.read('../.data/students-data/'+student)
            present_or_absent = input(f"{student_data['id']}    {student_data['first_name']} {student_data['last_name']}   is present? (P/A): ")

            if present_or_absent == "p" or present_or_absent == "P":
                present_or_absent = True
            if present_or_absent == "a" or present_or_absent == "A":
                present_or_absent = False

            present_data = {
                "date": date.strftime("%x"),
                "is_present": present_or_absent
            }
            if len(student_data['attendance']) > 0:
                for attendance in student_data['attendance']:
                    if attendance['date'] != date.strftime("%x"):
                        student_data['attendance'].append(present_data)
                        data.update('../.data/students-data/' + student, student_data)

            else:
                student_data['attendance'].append(present_data)
                data.update('../.data/students-data/' + student, student_data)

            return "Attendance Taken Complete"

    def update(self):
        student_id = input("Enter Student ID: ")
        if student_id:
            student_data = data.read('../.data/students-data/' + student_id+'.json')
            if type(student_data) == dict:

                if len(student_data['attendance']) > 0:
                    attendance_date = input("Enter Attendance Date (MM/DD/YY): ")
                    for attendance in student_data['attendance']:
                        if attendance['date'] == attendance_date:
                            is_present = input("Enter he/she is present? (P/A): ")
                            if is_present == "p" or is_present == "P":
                                is_present = True
                            if is_present == "a" or is_present == "A":
                                is_present = False
                            update_data = {
                                "date": attendance['date'],
                                "is_present": is_present
                            }
                            student_data['attendance'].remove(attendance)
                            student_data['attendance'].append(update_data)
                            data.update('../.data/students-data/' + student_id+'.json', student_data)
                            return "Attendance Updated"প[;'\/']

                else:
                    return "No attendance found"
            else:
                return "Student Not Found"
        else:
            return "No Student ID Entered"


s = Student_Attendance()
s.update()