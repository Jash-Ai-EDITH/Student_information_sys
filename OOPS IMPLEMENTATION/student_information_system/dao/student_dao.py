from dao.db_connection import DBConnection
from entity.student import Student

class StudentDAO:
    def __init__(self):
        self.db = DBConnection()

    def add_student(self, student):
        query = """
        INSERT INTO students (first_name, last_name, date_of_birth, email, phone_number)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            student.get_first_name(),
            student.get_last_name(),
            student.get_date_of_birth(),
            student.get_email(),
            student.get_phone_no()
        )

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

    def get_student_by_id(self, student_id):
        query = """
        SELECT student_id, first_name, last_name, date_of_birth, email, phone_number 
        FROM students 
        WHERE student_id = %s
        """

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (student_id,))
                row = cursor.fetchone()

        return Student(*row) if row else None

    def update_student_info(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        query = """
        UPDATE students 
        SET first_name = %s, last_name = %s, date_of_birth = %s, email = %s, phone_number = %s 
        WHERE student_id = %s
        """
        values = (first_name, last_name, date_of_birth, email, phone_number, student_id)

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

        print(f"Student {student_id} information updated successfully.")

