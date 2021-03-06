from hendler.student_registration import Student_Registration
from hendler.teacher_registration import Teacher_Registration
from hendler.student_payments import Student_Payments
from hendler.teacher_payments import Teacher_Payments
from hendler.student_attendance import Student_Attendance
from hendler.school_notice import Notice
from hendler.student_routine import Student_Routine
from hendler.all_student import all_student_red

student = Student_Registration()
teacher = Teacher_Registration()
student_payments = Student_Payments()
teacher_payments = Teacher_Payments()
student_attendance = Student_Attendance()
school_notice = Notice()
student_routine = Student_Routine()


def student_dashboard(data):
    bord_number = int(input('Enter Your Access Board Number: \n1. My Details\n2. My Class Routine\n3. My Attendance\n4. My Payments\n5. My Notice\n6. Logout\nEnter your choice: '))
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
    bord_number = int(input('Enter Your Access Board Number: \n1. My Details\n2. My Payments\n3. Add Notice\n4. Add Routine\n5. Call Student Attenaence\n6. Delete Routine\n7. Delete Notice\n8. Edit Attendance \n9. Logout\nEnter your choice: '))
    if bord_number == 1:
        print(f'\nID: {data["teacher_id"]}')
        print(f'Name: {data["first_name"]} {data["last_name"]}')
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            teacher_dashboard(data)
        print()

    elif bord_number == 2:
        payments_data = teacher_payments.read(data['teacher_id'])
        print()
        print(payments_data)
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            teacher_dashboard(data)
        # print()

    elif bord_number == 3:
        print()
        print(school_notice.add())
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            teacher_dashboard(data)
        print()

    elif bord_number == 4:
        print()
        print(student_routine.add())
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            teacher_dashboard(data)
        print()

    elif bord_number == 5:
        print()
        print(student_attendance.add())
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            teacher_dashboard(data)
        print()

    elif bord_number == 6:
        print()
        class_name = input("Enter Class: ")
        print(student_routine.delete(class_name))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            teacher_dashboard(data)
        print()

    elif bord_number == 7:
        print()
        notice_id = input("Enter Notice ID: ")
        print(school_notice.delete(notice_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            teacher_dashboard(data)
        print()

    elif bord_number == 8:
        print()
        student_id = input("Enter Student ID: ")
        print(student_attendance.update(student_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            teacher_dashboard(data)
        print()

    elif bord_number == 9:
        control()


def admin_dashboard():
    bord_number = int(input('Enter Your Access Board Number:\n1. Add Student \n2. Check Student Data \n3. Student Data Update \n4. Delete Student \n5.All Student \n6. Add Teacher \n7. Check Teacher \n8. Teacher Data Update \n9. Delete Teacher \n10. Add Notice \n11. Check Notice \n12. Notice Data Update \n13. Delete Notice \n14. Add Student Routine \n15. Update Student Routine \n16. Check Student Routine \n17. Delete Student Routine \n18. Add Student Payments \n19. Update Student Payments \n20. Check Student Payments \n21. Delete Student Payments  \n22. Add Teacher Payments \n23. Update Teacher Payments \n24. Check Teacher Payments \n25. Delete Teacher Payments \n26. Logout \nEnter your choice: '))

    if bord_number == 1:
        print()
        print(student.add())
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 2:
        print()
        student_id = input("Enter Your ID Number**: ")
        student_data = student.read(student_id)
        if type(student_data) == dict:
            print(f'\nID: {student_data["id"]}')
            print(f'Name: {student_data["first_name"]} {student_data["last_name"]}')
            print(f'Class: {student_data["class"]}')
            print(f'Roll: {student_data["roll"]}')
            print(f'Phone: {student_data["phone"]}')
            print(f'Address: {student_data["address"]}')
            print(f'E-mail: {student_data["email"]}')
        else:
            print("\nNo Data Found")
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 3:
        print()
        student_id = input("Enter Student ID: ")
        print(student.update(student_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 4:
        print()
        student_id = input("Enter Student ID: ")
        print(student.delete(student_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 5:
        print()
        print(all_student_red())
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 6:
        print()
        print(teacher.add())
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 7:
        print()
        teacher_id = input("Enter teacher ID: ")
        teacher_data = teacher.read(teacher_id)
        print(f'\nID: {teacher_data["teacher_id"]}')
        print(f'Name: {teacher_data["first_name"]} {teacher_data["last_name"]}')
        print(f"Email: {teacher_data['email']}")
        print(f"Phone: {teacher_data['phone']}")

        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 8:
        print()
        teacher_id = input("Enter teacher ID: ")
        print(teacher.update(teacher_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 9:
        print()
        teacher_id = input("Enter teacher ID: ")
        print(teacher.delete(teacher_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 10:
        print()
        print(school_notice.add())
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 11:
        print()
        print(school_notice.read())
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 12:
        print()
        notice_id = input("Enter notice ID: ")
        print(school_notice.update(notice_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 13:
        print()
        notice_id = input("Enter notice ID: ")
        print(school_notice.delete(notice_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 14:
        print()
        print(student_routine.add())
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 15:
        print()
        class_name = input("Enter class : ")
        print(student_routine.read(class_name))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 16:
        print()
        class_name = input("Enter class : ")
        print(student_routine.update(class_name))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 17:
        print()
        class_name = input("Enter class : ")
        print(student_routine.delete(class_name))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 18:
        print()
        print(student_payments.add())
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 19:
        print()
        student_id = input("Enter student id: ")
        print(student_payments.read(student_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 20:
        print()
        student_id = input("Enter student id: ")
        print(student_payments.update(student_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 21:
        print()
        student_id = input("Enter student id: ")
        print(student_payments.delete(student_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 22:
        print()
        print(teacher_payments.add())
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 23:
        print()
        teacher_id = input("Enter student id: ")
        print(teacher_payments.update(teacher_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 24:
        print()
        teacher_id = input("Enter student id: ")
        print(teacher_payments.read(teacher_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 25:
        print()
        teacher_id = input("Enter student id: ")
        print(teacher_payments.delete(teacher_id))
        print()
        go_back = input("\nPress 'y' to go back: ")
        if go_back == 'y' or go_back == 'Y':
            admin_dashboard()
        print()

    if bord_number == 26:
        control()


def control():
    Identity = int(input("\nEnter your identity: \n1. Student\n2. Teacher\n3. Admin\nEnter your choice: "))

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
            print()
            teacher_id = input("Enter Teacher Id Number**: ")
            data = teacher.read(teacher_id)
            if type(data) == dict:
                teacher_password = input("Enter your password: ")
                if data['password'] == teacher_password:
                    print("\nWelcome to your dashboard!\n")
                    teacher_dashboard(data)
                else:
                    print("\nWrong password!\nplease try again.")
                    control()

        elif is_registered == 2:
            control()

    elif Identity == 3:
        print()
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == 'admin' and password == '1234':
            print("\nWelcome to Admin dashboard!\n")
            print()
            admin_dashboard()
        else:
            print("\nWrong username or password!\nplease try again.")
            control()


    else:
        print("\nInvalid input")
        exit()


control()