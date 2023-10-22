# Введите ваше решение ниже
from random import randint


class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Name_person:

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: str):
        if type(value) != str or not value:
            raise InvalidNameError(
                f'Invalid name: {value}. Name should be a non-empty string.')
        setattr(instance, self.parameter_name, value)


class Age:
    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: int):
        if type(value) != int or value < 0:
            raise InvalidAgeError(
                f'Invalid age: {value}. Age should be a positive integer.')
        setattr(instance, self.parameter_name, value)


class Id_employee:
    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: int):
        if type(value) != int or value > 999999 or value < 100000:
            raise InvalidIdError(
                f'Invalid id: {value}. Id should be a 6-digit positive integer between 100000 and 999999.')
        setattr(instance, self.parameter_name, value)


class Person:
    age = Age()
    first_name = Name_person()
    lastname = Name_person()
    surname = Name_person()

    def __init__(self, lastname, first_name, surname, age):
        self.lastname = lastname
        self.first_name = first_name
        self.surname = surname
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def __str__(self):
        return f'{self.lastname} {self.first_name} {self.surname} - {self.age} лет'


class Employee(Person):
    ID_container = set()
    ID = Id_employee()

    def __init__(self, lastname, first_name, surname, age, em_id=randint(100000, 999999)):
        Person.__init__(self, lastname, first_name, surname, age)
        self.ID = em_id
        while True:
            if self.ID not in Employee.ID_container:
                Employee.ID_container.add(self.ID)
                break
            else:
                self.ID = randint(100000, 999999)

    def get_level(self):
        return sum(map(int, str(self.ID).split())) % 7

    def __str__(self):
        return f'ID: {self.ID} - {self.lastname} {self.first_name} {self.surname} - {self.age} лет'


t = Employee("Иванов", "Иван", "Иванович", 20)
print(t)
t1 = Employee("Иванова", "Иванна", "Ивановна", 5)
print(t1)
t1.birthday()
print(t1)
print(t1.get_level())
print(t.get_level())
#person = Person("", "John", "Doe", 30)
#person = Person("Alice", "Smith", "Johnson", -5)
#employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
person = Employee("Alice", "Smith", "Johnson", 25, 123456)
person2 = Employee("Alice", "Smith", "Smith", 25, 123456)
print(person.get_age())
print(Employee.ID_container)
print(person2)