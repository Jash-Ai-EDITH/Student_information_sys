class Student:
    def __init__(self, student_id, first_name, last_name, dob, email, phone):
        self.__student_id = student_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__email = email
        self.__phone = phone
        self.__payments = []


    def get_student_id(self):
        return self.__student_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__dob

    def get_email(self):
        return self.__email

    def get_phone_no(self):
        return self.__phone

    def get_payments(self):
        return self.__payments

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_date_of_birth(self, dob):
        self.__dob = dob

    def set_email(self, email):
        self.__email = email

    def set_phone_no(self, phone):
        self.__phone = phone
