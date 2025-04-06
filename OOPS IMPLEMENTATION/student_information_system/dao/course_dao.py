from dao.db_connection import DBConnection
from entity.course import Course

class CourseDAO:
    def __init__(self):
        self.db = DBConnection()

    def add_course(self, course):
        query = "INSERT INTO courses (course_name,course_code,credits,teacher_id) VALUES (%s, %s, %s,%s)"
        values = (
            course.get_course_name(),
            course.get_course_code(),
            course.get_credits(),
            course.get_teacher_id()
        )

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

    def get_course_by_id(self, course_id):
        query = """
        SELECT course_id, course_name, credits, teacher_id 
        FROM courses 
        WHERE course_id = %s
        """

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (course_id,))
                row = cursor.fetchone()

        return Course(*row) if row else None

    def assign_teacher(self, course_id, teacher_id):
        query = "UPDATE courses SET teacher_id = %s WHERE course_id = %s"
        values = (teacher_id, course_id)

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

        print(f"Teacher ID {teacher_id} assigned to Course ID {course_id}.")

    def update_course_info(self, course_id, course_name, credits, teacher_id):
        query = """
        UPDATE courses 
        SET course_name = %s, credits = %s, teacher_id = %s 
        WHERE course_id = %s
        """
        values = (course_name, credits, teacher_id, course_id)

        with self.db.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, values)
                connection.commit()

        print(f"Course {course_id} information updated successfully.")
