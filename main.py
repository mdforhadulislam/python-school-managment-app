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


def control():
    Identity = int(input("\nEnter your identity: \n1. Student\n2. Teacher\n3.Admin\nEnter your choice: "))
    if Identity == 1:
        is_registered = int(input("\nAre you registered?\n1. Yes\n2. No\nEnter your choice: "))

        if is_registered == 1:
            data = student.read()
            if type(data) == dict:
                pass
            else:
                print("\nEnter Valid Information")
                control()

        elif is_registered == 2:
            pass
        else:
            print("\nInvalid choice")

    elif Identity == 2:
        pass

    elif Identity == 3:
        pass

    else:
        print("\nInvalid input")
        exit()


control()