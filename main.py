from hendler.exam__routine import ExamRoutine
from hendler.notice import Notice
from hendler.routine import Routine
from hendler.student__login import Student
from hendler.student__payments import StudentPayments
from hendler.teacher__login import Teacher
from hendler.teacher__payments import TeacherPayments

# this class always working  teacher class
teacher = Teacher()
# this class always working  teacher added
# get teacher
# update teacher data
# delete teacher data

# this class always working  teacher payments
teacher__payments = TeacherPayments()
# when teacher want to pay crate teacher payments
# get teacher payments
# update teacher payments add another payment
# delete teacher payments
teacher__payments.delete_payments()


# this class is student class
student = Student()
# this class always working create student
# get student
# update student data
# delete student data

# this class always working  student payments
student__payments = StudentPayments()
# when student want to pay crate student payments
# get student payments
# update student payments add another payment
# delete student payments


# this class student routines
routine = Routine()
# teacher always create student routine
# student always get routine
# teacher always update routine
# teacher always delete routine


# this class student exam routine
exam__routine = ExamRoutine()
# teacher always create student exam routine
# student always get exam routine
# teacher always update exam routine
# teacher always delete exam routine


# this class working notice
notice = Notice()
# teacher always crate notice
# student always get notice
# teacher always update notice
# teacher always delete notice


# identity = input("What is your identity: \n" +
#                  "1.Teacher \n" + "2.Student \n" + "3.Admin \n")
