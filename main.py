from operator import truediv
from venv import create

from hendler.exam__routine import ExamRoutine
from hendler.notice import Notice
from hendler.routine import Routine
from hendler.student__login import Student
from hendler.student__payments import StudentPayments
from hendler.teacher__login import Teacher
from hendler.teacher__payments import TeacherPayments

# this class alaways working  teacher class
teacher = Teacher()
# this class alaways working  teacher added
# get teacher
# update teacher data
# delete teacher data

# this class alaways working  teacher payments
teacher__payments = TeacherPayments()
# when teacher want to pay crate teacher payments
# get teacher payments
# update teacher payments add another payment
# delete teacher payments


# this class is student class
student = Student()
# this class alaways working create student
# get student
# update student data
# delete student data

# this class alaways working  student payments
student__payments = StudentPayments()
# when student want to pay crate student payments
# get student payments
# update student payments add another payment
# delete student payments


# this class student routines
routine = Routine()
# teacher alaways create student routine
# student awalys get routine
# teacher awalys update routine
# teacher awalys delete routine


# this class student exam routine
exam__routine = ExamRoutine()
# teacher alaways create student exam routine
# student awalys get exam routine
# teacher awalys update exam routine
# teacher awalys delete exam routine


# this class working notice
notice = Notice()
# teacher alaways crate notice
# student awalys get notice
# teacher awalys update notice
# teacher awalys delete notice


# teacher deshbord System
def teacher_deshbord():
    if type_password == password:
        dashbord = input("1.Add Student \n" + "2.Delete Student\n" +
                         "3.Update Student Datils \n" + "4.See Student Datils \n" + '5.See Specific Class Student\n' + "6.Calling Student Attendance\n"+"7.see Specific Student Attendence\n"+"8.Student Routine\n" + "9.Student Notice\n"+"10.Student Exam Routine\n" + "11.LogOut\n")

        if dashbord == "1":
            student_created = student.create_student()
            print(student_created)
            print('\n')
            if student_created == "Requested Data Problem":
                print("Please Try Again")
                teacher_deshbord()
            else:
                print(student_created)
                print("Register Successfully")
                print("Please Student LogIn Her Device")
                teacher_deshbord()

        elif dashbord == "2":
            respons = student.delete_student()
            print("\n"+respons+'\n')
            print("Please Enter Valid Student ID \n")
            teacher_deshbord()

        elif dashbord == "3":
            pass
        elif dashbord == "4":
            pass
        elif dashbord == "5":
            pass
        elif dashbord == "6":
            pass
        elif dashbord == "7":
            pass
        elif dashbord == "8":
            pass
        elif dashbord == "9":
            pass
        elif dashbord == "10":
            pass

    else:
        print("Password is not correct")


idendity = input("What is your identity: \n" +
                 "1.Teacher \n" + "2.Student \n" + "3.Admin \n")

if idendity == "1":
    # Teacher Related all work
    value = input("Are you login here? (y/n):")
    if value == "y" or value == "Y":
        value = True
    elif value == "n" or value == "N":
        value = False
    else:
        value = ""

    if value:
        finde_teacher_data = teacher.get_teacher()
        if finde_teacher_data == "server side Error":
            print("Teacher Not Found Please LogIn Teacher")
        else:
            id = finde_teacher_data["id"]
            password = finde_teacher_data["password"]

            type_password = input("Enter your password: ")
            print("\nWelcome Teacher\n")
            teacher_deshbord()
            print(finde_teacher_data)
    elif value == False:
        #  login school teacher
        crated = teacher.create_teacher()
        print('\n')
        if crated == "Requested Data Problem":
            print("Please Try Again")
        else:
            print(crated)
            print("Register Successfully")
            print("Please LogIn")


elif idendity == "2":
    pass
elif idendity == "3":
    pass
else:
    print("Enter valid identity")
