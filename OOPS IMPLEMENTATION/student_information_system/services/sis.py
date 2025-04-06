from dao.student_dao import StudentDAO
from dao.course_dao import CourseDAO
from dao.enrollment_dao import EnrollmentDAO
from dao.payment_dao import PaymentDAO
from dao.teacher_dao import TeacherDAO
from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher

import datetime

class SIS:
    def __init__(self):
        self.student_dao = StudentDAO()
        self.course_dao = CourseDAO()
        self.enrollment_dao = EnrollmentDAO()
        self.payment_dao = PaymentDAO()
        self.teacher_dao = TeacherDAO()

    def add_student(self, first_name, last_name, dob, email, phone):
        student = Student(None, first_name, last_name, dob, email, phone)
        self.student_dao.add_student(student)
        print("Student added successfully!")

    def enroll_student(self, student_id, course_id):
        enrollment_date = datetime.date.today()
        self.enrollment_dao.enroll_student(student_id, course_id, enrollment_date)
        print("Student enrolled successfully!")

    def add_course(self, course_name, course_code, instructor_name,credits):
        course = Course(None, course_name, course_code, instructor_name,credits)
        self.course_dao.add_course(course)
        print("Course added successfully!")

    def add_teacher(self, first_name, last_name, email, expertise):
        try:
            self.teacher_dao.insert_teacher(first_name, last_name, email, expertise)
            print("Teacher added successfully.")
        except Exception as e:
            print("Error adding teacher:", e)

    def assign_teacher(self, course_id, teacher_name):
        self.course_dao.assign_teacher(course_id, teacher_name)
        print("Teacher assigned successfully!")

    def record_payment(self, student_id, amount,payment_date):
        self.payment_dao.record_payment(student_id, amount, payment_date)
        print("Payment recorded successfully!")

    def view_student_enrollments(self, student_id):
        course_names = self.enrollment_dao.get_enrollments_for_student(student_id)
        if course_names:
            print(f"Student {student_id} is enrolled in: {', '.join(course_names)}")
        else:
            print(f"Student {student_id} is not enrolled in any courses.")

    def view_payments_by_student(self, student_id):
        payments = self.payment_dao.get_payments_for_student(student_id)
        if not payments:
            print("No payments found for this student.")
            return
        for payment in payments:
            print(f"Payment ID: {payment.get_payment_id()}, Amount: {payment.get_payment_amount()}, Date: {payment.get_payment_date()}")


    def update_student_info(self, student_id, first_name, last_name, dob, email, phone):
        try:
            self.student_dao.update_student_info(student_id, first_name, last_name, dob, email, phone)
            print(f"Student (ID: {student_id}) updated successfully.")
        except Exception as e:
            print(f"Error updating student: {e}")

    def update_course_info(self, course_id, course_code, course_name, instructor_name):

        try:
            self.course_dao.update_course_info(course_id, course_code, course_name, instructor_name)
            print(f"Course (ID: {course_id}) updated successfully.")
        except Exception as e:
            print(f"Error updating course: {e}")

    def update_teacher_info(self, teacher_id, first_name, last_name, email,expertise):
        try:
            self.teacher_dao.update_teacher_info(teacher_id, first_name, last_name, email,expertise)
            print(f"Teacher (ID: {teacher_id}) updated successfully.")
        except Exception as e:
            print(f"Error updating teacher: {e}")

    def generate_enrollment_report(self, course_name):
        students = self.enrollment_dao.get_enrollments_by_course(course_name)
        if not students:
            print(f"No enrollments found for course: {course_name}")
            return
        print(f"\nEnrollment Report for {course_name}")
        print("-" * 50)
        for student in students:
            print(f"Student ID: {student[0]}, Name: {student[1]} {student[2]}, Email: {student[3]}")
        print("-" * 50)

