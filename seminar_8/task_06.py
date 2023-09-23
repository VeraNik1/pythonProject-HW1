"""Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла."""

import csv
import pickle

PATH_FILE = 'users_data_new.pickle'
PATH_CSV = 'users_data_new.csv'


def from_pickle_to_csv(path):
    with open(path, 'rb') as file:
        new_dict = pickle.load(file)
    csv_headers = new_dict.keys()
    csv_table = new_dict.values()
    csv_table = list(zip(*csv_table))
    with open(PATH_CSV, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, dialect='excel', delimiter=' ')
        file_writer.writerow(csv_headers)
        file_writer.writerows(csv_table)


if __name__ == '__main__':
    from_pickle_to_csv(PATH_FILE)
