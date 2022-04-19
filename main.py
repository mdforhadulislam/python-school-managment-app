from hendler.student_registration import Student_Registration
from hendler.teacher_registration import Teacher_Registration
from hendler.student_payments import Student_Payments
from hendler.teacher_payments import Teacher_Payments
from hendler.student_attendance import Student_Attendance
from hendler.school_notice import Notice
from hendler.student_routine import Student_Routine

student = Student_Registration()
teacher = Teacher_Registration()
student_payments = Student_Payments()
teacher_payments = Teacher_Payments()
student_attendance = Student_Attendance()
school_notice = Notice()
student_routine = Student_Routine()


def student_dashboard(data):
    bord_number = int(input('Enter Your Access Board Number: \n1.My Details\n2.My Class Routine\n3.My Attendance\n4.My Payments\n5.My Notice\n6.Logout\nEnter your choice: '))
    if bord_number == 1:
        student_data = student.read(data['id'])
        print(f'\nID: {student_data["id"]}')
        print(f'Name: {student_data["first_name"]} {student_data["last_name"]}')
        print(f'Class: {student_data["class"]}')
        print(f'Roll: {student_data["roll"]}')
        print(f'Phone: {student_data["phone"]}')
        print(f'Address: {student_data["address"]}')
        print(f'E-mail: {student_data["email"]}')

        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            student_dashboard(data)
        print()

    elif bord_number == 2:
        routine_data = student_routine.read(data['class'])
        print()
        print(routine_data)
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            student_dashboard(data)
        print()

    elif bord_number == 3:
        attendance_data = student_attendance.read(data['id'])
        print()
        print(attendance_data)
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            student_dashboard(data)
        print()

    elif bord_number == 4:
        payments_data = student_payments.read(data['id'])
        print()
        print(payments_data)
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            student_dashboard(data)
        print()

    elif bord_number == 5:
        notice_data = school_notice.read()
        print(notice_data)
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            student_dashboard(data)
        print()

    elif bord_number == 6:
        control()


def teacher_dashboard(data):
    


def control():
    Identity = int(input("\nEnter your identity: \n1. Student\n2. Teacher\n3.Admin\nEnter your choice: "))
    if Identity == 1:
        is_registered = int(input("\nAre you registered?\n1. Yes\n2. No\nEnter your choice: "))

        if is_registered == 1:
            print()
            student_id = input("Enter Your ID Number**: ")
            data = student.read(student_id)
            if type(data) == dict:
                student_password = input("Enter your password: ")
                if data['password'] == student_password:
                    print("\nWelcome to your dashboard!\n")
                    student_dashboard(data)
                else:
                    print("\nWrong password!\nplease try again.")
                    control()
            else:
                print("\nEnter Valid Information")
                control()

        elif is_registered == 2:
            print()
            print(student.add())
            control()
        else:
            print("\nInvalid choice\n")
            control()

    elif Identity == 2:
        is_registered = int(input("\nAre you registered?\n1. Yes\n2. No\nEnter your choice: "))
        if is_registered == 1:
            teacher_dashboard()

        elif is_registered == 2:
            control()


    elif Identity == 3:
        pass

    else:
        print("\nInvalid input")
        exit()


control()