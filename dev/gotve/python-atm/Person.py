class Person:

    def __init__(self, age):
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_first_name(self, first_name):
        self.__name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name
