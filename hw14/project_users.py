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

from hw14.user_errors import AccessError, LevelError



def login(name: str,
          user_id: str) -> str:  # authorisation of user. If user in the set user_list we get his level
    login_user = User(name, user_id)
    for user in UserWorkshop.user_list:
        if login_user == user:  # checking user equality with __eq__ и __hash__ in the class User (users are
            # equal when users' name and id are equal
            return user.level
    else:
        raise AccessError(name)  # raise access error in module user_errors.py


class UserWorkshop:
    user_list = set()

    def __init__(self):
        UserWorkshop.load_users()
        pass

    @staticmethod
    def load_users(path: str = 'users_data.json'):
        with open(path, 'r', encoding='UTF-8') as f:
            user_dict = json.load(f)
        for level, user_list in user_dict.items():
            for user_id, name in user_list.items():
                UserWorkshop.user_list.add(
                    User(name, str(user_id), str(level)))  # create user object and add it to the set of users

    def create_user(self, name: str, user_id: str, level: str):  # create user if level of new user lower than level
        # of authorised user
        cur_name, cur_id = input(
            "Input user name and user id divided by whitespace").split()  # authorisation of user from
        # users_list
        if current_level := login(cur_name, cur_id):  # if user exists and his level != 0
            if int(current_level) > int(level):
                return User(name, user_id,
                            level)  # create new user, if the level of authorised user more than level of new user
            else:
                raise LevelError(current_level, level)


b = UserWorkshop()
print(login('Petrov', '1'))  # (name, id)  level = 5
print(b.create_user('New_user', '1',
                    '3'))  # making new user (name, id, level) if new user's level less than level of logged user
