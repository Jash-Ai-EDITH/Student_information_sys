class Course:
    def __init__(self, course_id, course_name, course_code, instructor_name, credits):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__course_code = course_code
        self.__instructor_name = instructor_name
        self.__students_enrolled = []
        self.__teacher = None
        self.__credits = credits


    def assign_teacher(self, teacher):
        self.__teacher = teacher

    def update_course_info(self, course_code, course_name, instructor_name):
        self.__course_code = course_code
        self.__course_name = course_name
        self.__instructor_name = instructor_name

    def display_course_info(self):
        print(f"Course: {self.__course_name} ({self.__course_code}), Instructor: {self.__instructor_name}")

    def get_enrollments(self):
        return self.__students_enrolled

    def get_teacher_id(self):
        return self.__instructor_name

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def get_course_code(self):
        return self.__course_code

    def get_instructor_name(self):
        return self.__instructor_name

    def get_credits(self):
        return self.__credits