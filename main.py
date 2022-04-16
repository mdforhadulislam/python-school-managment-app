from hendler.student_registration import Student_Registration
from hendler.teacher_registration import Teacher_Registration
from hendler.student_payments import Student_Payments
from hendler.teacher_payments import Teacher_Payments

student = Student_Registration()
teacher = Teacher_Registration()
student_payments = Student_Payments()
teacher_payments = Teacher_Payments()

# print(student.add())
print(teacher_payments.update())

