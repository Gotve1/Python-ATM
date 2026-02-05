class Person:

    def __init__(self):
        self.__age = 0
        self.__first_name = ''
        self.__last_name = ''

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def firstname(self):
        return self.__first_name

    @firstname.setter
    def firstname(self, first_name):
        self.__first_name = first_name

    @property
    def lastname(self):
        return self.__last_name

    @lastname.setter
    def lastname(self, last_name):
        self.__last_name = last_name