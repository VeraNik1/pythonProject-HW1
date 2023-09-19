"""Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
📌После каждого ввода добавляйте новую информацию в JSON файл.
📌Пользователи группируются по уровню доступа.
📌Идентификатор пользователя выступает ключём для имени.
📌Убедитесь, что все идентификаторы уникальны независимо от
уровня доступа.
📌При перезапуске функции уже записанные в файл данные должны сохраняться."""

import json
import pathlib

FILE_PATH = pathlib.Path("users_data.json")


def load_json_file(file_name):
    temp_dict = {}
    if file_name.exists():
        with open(file_name, 'r', encoding="UTF-8") as file:
            temp_dict = json.load(file)
    return temp_dict


def rewrite_json_file(file_name, data):
    with open(file_name, 'w+', encoding="UTF-8") as file:
        print(json.dumps(data, ensure_ascii=True, separators=(',', ':')), file=file)


def user_name():
    while True:
        name = input("Введите имя: >>>  ")
        if not name:
            continue
        return name


def user_id(data_id):
    while True:
        u_id = input("Введите ID: >>>  ")
        if u_id in data_id:
            print("Введенный ID занят")
            continue
        return u_id


def level():
    while True:
        try:
            u_level = int(input("Введите уровень доступа: >>>  "))
            if 0 < u_level < 8:
                return str(u_level)
            continue
        except:
            print("Введите число от 1 до 7")


def users_list():
    global FILE_PATH
    data = load_json_file(FILE_PATH)
    id_data = set()

    while True:
        for v in data.values():
            for k in v:
                id_data.add(k)
        name = user_name()
        uid = user_id(id_data)
        lvl = level()
        data[lvl] = data.get(lvl, {}) | {uid: name}
        #print(data)
        rewrite_json_file(FILE_PATH, data)
        if input("Введите q для выхода или любую клавишу чтобы продолжить>>> ").lower() == 'q':
            return


users_list()
