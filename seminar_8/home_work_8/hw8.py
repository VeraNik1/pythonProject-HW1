"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в  файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов
и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов."""

import os
import json
import csv
import pickle


def get_dir_size(path: str) -> int:
    total_size = 0
    for root, directory, files in os.walk(path):
        for file in files:
            fp = os.path.join(root, file)
            total_size += os.path.getsize(fp)
    return total_size


def get_objects_data(path: str) -> list:
    if os.name == 'nt':
        delimiter = '\\'
    else:
        delimiter = '/'
    result_list = []
    for root, directory, files in os.walk(os.path.abspath(path)):
        for dir_name in directory:
            dir_info = {"name": dir_name,
                        "parent_directory": root.split(delimiter)[-1],
                        "object_type": 'directory',
                        "size_byte": get_dir_size(os.path.join(root, dir_name))}
            result_list.append(dir_info)
        for file in files:
            file_info = {"name": file,
                         "parent_directory": root.split(delimiter)[-1],
                         "object_type": 'file',
                         "size_byte": os.path.getsize(os.path.join(root, file))}
            result_list.append(file_info)
    return result_list


def save_to_json(info_lst: list, output_file: str = "directory_stats.json"):
    with open(output_file, "w") as js_f:
        json.dump(info_lst, js_f, indent=4, ensure_ascii=False)


def save_to_csv(info_lst: list, output_file: str = "directory_stats.csv"):
    with open(output_file, "w", newline="") as csv_f:
        fieldnames = ["name", "parent_directory", "object_type", "size_byte"]
        writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(info_lst)


def save_to_pickle(info_lst: list, output_file: str = "directory_stats.pickle"):
    with open(output_file, "wb") as pickle_f:
        pickle.dump(info_lst, pickle_f)


def get_dir_info(directory):
    info_list = get_objects_data(directory)
    save_to_json(info_list)
    save_to_csv(info_list)
    save_to_pickle(info_list)


if __name__ == '__main__':
    get_dir_info("..")
