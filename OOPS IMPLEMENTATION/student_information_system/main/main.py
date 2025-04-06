try:
    from services.sis import SIS
except ModuleNotFoundError:
    print("Module 'sis.py' not found. Please ensure it is located in the correct directory.")


def main():
    sis = SIS()

    while True:

        print("*-*" * 10)
        print("Student Information System")
        print("*-*" * 10)
        print("1. Add new student ")
        print("2. Add Course")
        print("3. Add Teacher ")
        print("4. Enroll Student")
        print("5. Assign Teacher")
        print("6. Record Payment")
        print("7. View Payments by Student")
        print("8. View Student Enrollments")
        print("9. Update Course Information")
        print("10.Update Student Information")
        print("11.Update Teacher Information")
        print("12.Enrollment report")
        print("0.>>>> Exit <<<<")
        print("*_*_" * 10)
        choice = input("Enter your choice: ")
        print("*_*_" * 10)

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            email = input("Email: ")
            phone = input("Phone Number: ")
            sis.add_student(first_name, last_name, dob, email, phone)

        elif choice == '2':
            course_name = input("Course Name: ")
            course_code = input("Course id: ")
            credits = int(input("Number of Credits: "))
            instructor_name = input("teacher id: ")
            sis.add_course(course_name, course_code, instructor_name,credits)


        elif choice == '3':
            first_name = input("Teacher First Name: ")
            last_name = input("Teacher Last Name: ")
            email = input("Teacher Email: ")
            expertise = input("Teacher Expertise: ")
            sis.add_teacher(first_name, last_name, email, expertise)

        elif choice == '4':
            student_id = int(input("Student ID: "))
            course_id = int(input("Course ID: "))
            sis.enroll_student(student_id, course_id)

        elif choice == '5':
            course_id = int(input("Course ID: "))
            teacher_name = input("Teacher Name: ")
            sis.assign_teacher(course_id, teacher_name)


        elif choice == '6':
            student_id = int(input("Student ID: "))
            amount = float(input("Payment Amount: "))
            payment_date = input("Enter Payment Date (YYYY-MM-DD): ")
            sis.record_payment(student_id, amount, payment_date)


        elif choice == '7':
            student_id = int(input("Student ID: "))
            sis.view_payments_by_student(student_id)

        elif choice == '8':
            student_id = int(input("Student ID: "))
            sis.view_student_enrollments(student_id)

        elif choice == '9':
            course_id = int(input("Course ID: "))
            course_code = input("Updated Course Code: ")
            course_name = input("Updated Course Name: ")
            instructor_name = input("Updated Instructor Name: ")
            sis.update_course_info(course_id, course_code, course_name, instructor_name)

        elif choice == '10':
            student_id = int(input("Student ID: "))
            first_name = input("Updated First Name: ")
            last_name = input("Updated Last Name: ")
            dob = input("Updated Date of Birth (YYYY-MM-DD): ")
            email = input("Updated Email: ")
            phone = input("Updated Phone Number: ")
            sis.update_student_info(student_id, first_name, last_name, dob, email, phone)

        elif choice == '11':
            teacher_id = int(input("Teacher ID: "))
            first_name = input("Updated First Name: ")
            last_name = input("Updated Last Name: ")
            email = input("Updated Email: ")
            expertise = input("updated Teacher Expertise: ")
            sis.update_teacher_info(teacher_id, first_name, last_name, email,expertise)

        elif choice == '12':
            course_name = input("Enter Course Name for Report: ")
            sis.generate_enrollment_report(course_name)

        elif choice == '0':
            print("Application terminated. Thank you for using the system.")
            break

        else:
            print("Invalid option selected. Please enter a valid choice.")


if __name__ == "__main__":
    main()