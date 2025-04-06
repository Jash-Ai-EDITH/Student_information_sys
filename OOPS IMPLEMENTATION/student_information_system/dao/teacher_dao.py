from dao.db_connection import DBConnection
from entity.teacher import Teacher

class TeacherDAO:
    def __init__(self):
        self.db = DBConnection()

    def add_teacher(self, teacher):
        query = "INSERT INTO teachers (first_name, last_name, email, expertise) VALUES (%s, %s, %s, %s)"
        values = (teacher.get_first_name(), teacher.get_last_name(), teacher.get_email(), teacher.get_expertise())

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

        print(f"Teacher {teacher.get_first_name()} {teacher.get_last_name()} added successfully.")

    def get_teacher_by_id(self, teacher_id):
        query = "SELECT teacher_id, first_name, last_name, email FROM teachers WHERE teacher_id = %s"

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (teacher_id,))
                row = cursor.fetchone()

        return Teacher(*row) if row else None

    def update_teacher_info(self, teacher_id, first_name, last_name, email, expertise):
        query = """
        UPDATE teachers 
        SET first_name = %s, last_name = %s, email = %s, expertise = %s
        WHERE teacher_id = %s
        """
        values = (first_name, last_name, email, expertise, teacher_id)

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

        print(f"Teacher {teacher_id} information updated successfully.")

