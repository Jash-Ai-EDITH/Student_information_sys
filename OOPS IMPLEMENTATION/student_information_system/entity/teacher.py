class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.__teacher_id = teacher_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__assigned_courses = []

    def update_teacher_info(self, first_name, last_name, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    def display_teacher_info(self):
        print(f"Teacher: {self.__first_name} {self.__last_name}, Email: {self.__email}")

    def get_assigned_courses(self):
        return self.__assigned_courses

    def get_teacher_id(self):
        return self.__teacher_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_expertise(self):
        return self.expertise
