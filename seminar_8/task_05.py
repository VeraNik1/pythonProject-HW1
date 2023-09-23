"""Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов"""

import json
import os
import pickle


def json_to_pickle(path: str = os.getcwd()):
    file_list = []
    for files in os.walk(path):
        for file in files[2]:
            if file.endswith('.json'):
                file_list.append(((os.path.join(files[0], file),
                                   os.path.join(files[0], file.rsplit('.')[0] + '.pickle'))))
    for file in file_list:
        with open(file[0], 'r', encoding='UTF-8') as f_in:
            data = json.load(f_in)
        with open(file[1], 'wb') as f_out:
            pickle.dump(data, f_out)


if __name__ == '__main__':
    json_to_pickle()