class Person:
    __age: int
    __first_name: str
    __last_name: str

    def __init__(self, first_name: str = "", last_name: str = "", age: int = 0):
        self.__age = age
        self.__first_name = first_name
        self.__last_name = last_name

    def set_age(self, age):
        self.__age = age
        return self

    def get_age(self):
        return self.__age

    def set_firstname(self, first_name):
        self.__first_name = first_name
        return self

    def get_firstname(self):
        return self.__first_name

    def set_lastname(self, last_name):
        self.__last_name = last_name
        return self

    def get_lastname(self):
        return self.__last_name
