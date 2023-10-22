"""
Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""
import json
from hw14.user import User

from hw14.user_errors import *


class UserWorkshop:
    user_list = set()

    def __init__(self):
        UserWorkshop.load_users()
        self.current_user = User('test', '0', '0')

    @staticmethod
    def load_users(path: str = 'users_data.json'):
        with open(path, 'r', encoding='UTF-8') as f:
            user_dict = json.load(f)
        for level, user_list in user_dict.items():
            for user_id, name in user_list.items():
                UserWorkshop.user_list.add(
                    User(name, str(user_id), str(level)))  # create user object and add it to the set of users

    def create_user(self, new_name, new_level):  # create user if level of new user lower than level
        # of authorised user

        if int(new_level) <= int(self.current_user.level):
            new_id = str(max(map(int, [user.user_id for user in self.user_list])) + 1)
            self.user_list.add(User(new_name, new_id, new_level))
            return new_level  # create new user, if the level of authorised user more than level of new user
        else:
            raise LevelError(f"Ошибка уровня - {new_level} > минимального уровня {self.current_user.level}")

    def login(self, name: str,
              user_id: str) -> str:  # authorisation of user. If user in the set user_list current_user = authorized user
        logging_user = User(name, user_id)
        for user in self.user_list:
            if logging_user == user:  # checking user equality with __eq__ и __hash__ in the class User (users are
                # equal when users' name and id are equal
                self.current_user = User(name, user_id, user.level)
                return self.current_user.level

        raise AccessError(f"Ошибка доступа - {name}")  # raise access error in module user_errors.py




