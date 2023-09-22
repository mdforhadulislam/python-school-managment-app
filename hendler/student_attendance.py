from lib.data import Data
from lib.utilities import list_files
import datetime


data = Data()
date = datetime.datetime.now()
student_files = list_files('.data/students-data/')


class Student_Attendance:
    def __init__(self):
        self.name = "Student Attendance"

    def add(self):
        for student in student_files:
            student_data = data.read(f'.data/students-data/{student}')
            present_or_absent = input(f"{student_data['id']}    {student_data['first_name']} {student_data['last_name']}   is present? (P/A): ") or "A "

            if present_or_absent in ["p", "P"]:
                present_or_absent = True
            if present_or_absent in ["a", "A"]:
                present_or_absent = False

            present_data = {
                "date": date.strftime("%x"),
                "is_present": present_or_absent
            }
            if len(student_data['attendance']) > 0:
                for attendance in student_data['attendance']:
                    if attendance['date'] != date.strftime("%x"):
                        student_data['attendance'].append(present_data)
                        data.update(f'.data/students-data/{student}', student_data)

            else:
                student_data['attendance'].append(present_data)
                data.update(f'.data/students-data/{student}', student_data)
        print("Attendance Taken Complete")

    def read(self, student_id):
        global present
        if not student_id:
            return "Enter Student ID"
        student_data = data.read(f'.data/students-data/{student_id}.json')
        if type(student_data) != dict:
            return "Student Not Found"
        if len(student_data['attendance']) > 0:
            for attendance in student_data['attendance']:
                present = "Present" if attendance["is_present"] else "Absent"
                print(f'{attendance["date"]} he/she is {present}')

    def update(self, student_id):
        if not student_id:
            return "No Student ID Entered"
        student_data = data.read(f'.data/students-data/{student_id}.json')
        if type(student_data) != dict:
            return "Student Not Found"
        if len(student_data['attendance']) <= 0:
            return "No attendance found"
        attendance_date = input("Enter Attendance Date (MM/DD/YY): ")
        for attendance in student_data['attendance']:
            if attendance['date'] == attendance_date:
                is_present = input("Enter he/she is present? (P/A): ")
                if is_present in ["p", "P"]:
                    is_present = True
                if is_present in ["a", "A"]:
                    is_present = False
                update_data = {
                    "date": attendance['date'],
                    "is_present": is_present
                }
                student_data['attendance'].remove(attendance)
                student_data['attendance'].append(update_data)
                data.update(f'.data/students-data/{student_id}.json', student_data)
                return "Attendance Updated"

    def delete(self):
        if not (student_id := input("Enter Student ID: ")):
            return "Enter Student ID"
        student_data = data.read(f'.data/students-data/{student_id}.json')
        if type(student_data) != dict:
            return "Student Not Found"
        if len(student_data['attendance']) > 0:
            attendance_date = input("Enter Attendance Date (MM/DD/YY): ")
            for attendance in student_data['attendance']:
                if attendance['date'] == attendance_date:
                    student_data['attendance'].remove(attendance)
                    data.update(f'.data/students-data/{student_id}.json', student_data)
                    return "Attendance Deleted"

