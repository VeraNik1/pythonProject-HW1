"""
Задание №4
Из json файла берутся данные для создания класса пользователей, и из класса множества  пользователей
"""

from hw14.user_errors import *


class Name_user:

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: str):
        if type(value) != str or not value:
            raise InvalidNameError(
                f'Invalid name: {value}. Name should be a non-empty string.')
        setattr(instance, self.parameter_name, value)


class Level:
    MAX_LEVEL = 20

    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: str):
        if type(value) != str or not value.isdigit() or int(value) < 0 or int(value) > Level.MAX_LEVEL:
            raise InvalidLevelError(
                f'Invalid level: {value}. Level should be a positive digit less than {Level.MAX_LEVEL}.')
        setattr(instance, self.parameter_name, value)


class Id_user:
    def __set_name__(self, owner, name):
        self.parameter_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parameter_name)

    def __set__(self, instance, value: str):
        if type(value) != str or not value.isdigit() or int(value) < 0:
            raise InvalidIdError(
                f'Invalid id: {value}. Id should be a positive digit')
        setattr(instance, self.parameter_name, value)


class User:
    name = Name_user()
    level = Level()
    user_id = Id_user()

    def __init__(self, name: str, user_id: str, level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __str__(self):
        return f'User: name: {self.name}, id: {self.user_id},  level: {self.level}'

    def __repr__(self):
        return f'User: {self.name}, {self.user_id},  {self.level}'

    def __hash__(self):  # при переопределениии eq надо переопределять hash
        return hash(self.name) + hash(self.user_id)

    def __eq__(self, other):  # True/False в зависимоти от выполнения условий
        return self.name == other.name and self.user_id == other.user_id
