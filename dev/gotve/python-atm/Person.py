class Person:

    __age: int
    __first_name: str
    __last_name: str

    def __init__(self):
        pass

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_firstname(self, first_name):
        self.__first_name = first_name

    def get_firstname(self):
        return self.__first_name

    def set_lastname(self, last_name):
        self.__last_name = last_name

    def get_lastname(self):
        return self.__last_name
