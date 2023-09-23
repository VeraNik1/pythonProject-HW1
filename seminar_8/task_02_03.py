"""
Задание №2
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
📌После каждого ввода добавляйте новую информацию в JSON файл.
📌Пользователи группируются по уровню доступа.
📌Идентификатор пользователя выступает ключём для имени.
📌Убедитесь, что все идентификаторы уникальны независимо от
уровня доступа.
📌При перезапуске функции уже записанные в файл данные должны сохраняться.

Задание №3
📌Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""

import json
import pathlib
import csv

FILE_PATH_JSON = pathlib.Path("users_data.json")


def load_json_file(file_name):
    temp_dict = {}
    if file_name.exists():
        with open(file_name, 'r', encoding="UTF-8") as file:
            temp_dict = json.load(file)
    return temp_dict


def rewrite_json_file(file_name, data):
    with open(file_name, 'w+', encoding="UTF-8") as file:
        json.dump(data, file)


def from_json_to_csv(file_name):
    with (open(file_name, 'r', encoding="UTF-8") as f_json,
          open(f'{file_name.stem}.csv', 'w+', encoding="UTF-8") as f_csv
          ):
        read_json = json.load(f_json)
        csv_writer = csv.writer(f_csv, delimiter=",", lineterminator="\r")
        csv_writer.writerow(("ID", "Name", "Access level"))
        for lvl, values in read_json.items():
            for u_id, name in values.items():
                csv_writer.writerow([u_id, name, lvl])


def user_name() -> str:
    while True:
        name = input("Введите имя: >>>  ")
        if not name:
            continue
        return name


def user_id(data_id: set) -> str:
    while True:
        try:
            u_id = abs(int(input("Введите ID: >>>  ")))
            if str(u_id) in data_id:
                print("Введенный ID занят")
                continue
            else:
                return str(u_id)
        except:
            print("Введен некорректный ID, необходимо ввести натуральное число")
            continue



def level() -> str:
    while True:
        try:
            u_level = int(input("Введите уровень доступа: >>>  "))
            if 0 < u_level < 8:
                return str(u_level)
            continue
        except:
            print("Введите число от 1 до 7")


def users_list():
    global FILE_PATH_JSON
    data = load_json_file(FILE_PATH_JSON)
    id_data = set()

    while True:
        for v in data.values():
            for k in v:
                id_data.add(str(k))
        name = user_name()
        uid = user_id(id_data)
        lvl = level()
        data[lvl] = data.get(lvl, {}) | {uid: name}
        # print(data)
        rewrite_json_file(FILE_PATH_JSON, data)
        if input("Введите q для выхода или любую клавишу чтобы продолжить>>> ").lower() == 'q':
            return


users_list()
from_json_to_csv(FILE_PATH_JSON)
