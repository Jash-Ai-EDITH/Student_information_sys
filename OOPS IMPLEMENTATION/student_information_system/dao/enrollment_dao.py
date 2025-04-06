from dao.db_connection import DBConnection

class EnrollmentDAO:
    def __init__(self):
        self.db = DBConnection()

    def enroll_student(self, student_id, course_id, enrollment_date):
        try:
            with self.db.get_connection() as connection:
                with connection.cursor() as cursor:
                    check_query = """
                        SELECT COUNT(*) FROM enrollments 
                        WHERE student_id = %s AND course_id = %s
                    """
                    cursor.execute(check_query, (student_id, course_id))
                    (count,) = cursor.fetchone()

                    if count > 0:
                        print(f" Error: Student {student_id} is already enrolled in Course {course_id}.")
                        return

                    # Insert enrollment
                    query = """
                        INSERT INTO enrollments (student_id, course_id, enrollment_date) 
                        VALUES (%s, %s, %s)
                    """
                    values = (student_id, course_id, enrollment_date)
                    cursor.execute(query, values)
                    connection.commit()
                    print("Student enrolled successfully!")

        except Exception as e:
            print(f"Error enrolling student: {e}")

    def get_enrollments_for_student(self, student_id):
        query = """
        SELECT c.course_name
        FROM enrollments e
        JOIN courses c ON e.course_id = c.course_id
        WHERE e.student_id = %s
        """

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (student_id,))
                rows = cursor.fetchall()

        return [row[0] for row in rows]

    def get_students_by_course(self, course_id):
        query = """
        SELECT s.student_id, s.first_name, s.last_name, s.email
        FROM enrollments e
        JOIN students s ON e.student_id = s.student_id
        WHERE e.course_id = %s
        """

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (course_id,))
                rows = cursor.fetchall()

        return [{"Student ID": row[0], "Name": f"{row[1]} {row[2]}", "Email": row[3]} for row in rows]

    def get_enrollments_by_course(self, course_name):
        query = """
        SELECT s.student_id, s.first_name, s.last_name, s.email 
        FROM enrollments e
        JOIN students s ON e.student_id = s.student_id
        JOIN courses c ON e.course_id = c.course_id
        WHERE c.course_name = %s
        """

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (course_name,))
                rows = cursor.fetchall()

        return rows
