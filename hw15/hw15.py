"""
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
    ○ имя файла без расширения или название каталога,
    ○ расширение, если это файл,
    ○ флаг каталога,
    ○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
"""

import os
import logging
from collections import namedtuple

file_info_ = namedtuple(
    "file_info_", ["obj_name", "extension", "is_directory", "parent_directory"])


def get_objects_data(path: str) -> list:
    """
    to get info about all directories and files in the directory with given path
    """
    if os.name == 'nt':
        delimiter = '\\'
    else:
        delimiter = '/'
    result_list = []
    for root, directory, files in os.walk(os.path.abspath(path)):
        # adding info about directories
        for obj_dir in directory:
            dir_name = os.path.basename(obj_dir)
            parent_dir = root.split(delimiter)[-1]
            result_list.append(file_info_(dir_name, None, True, parent_dir))

        # adding info about files
        for file in files:

            parent_dir = root.split(delimiter)[-1]

            if "." in file:
                *file_name, file_extension = file.split(".")
                file_name = ".".join(file_name)
            else:
                file_name = file
                file_extension = None

            result_list.append(file_info_(file_name, file_extension, False, parent_dir))
    return result_list


def create_log(path):
    """
    to make logfile for the directory with given path to directory with hw15
    """

    log_file_name = str(os.path.basename(path) + ".log")
    save_log_to = os.path.join("C:\\Users\\Veronika\\PycharmProjects\\pythonProject\\hw15", log_file_name)

    logging.basicConfig(filename=save_log_to, filemode="w",
                        encoding="UTF-8", level=logging.INFO)
    my_logger = logging.getLogger(__name__)
    res = get_objects_data(path)
    for r in res:
        my_logger.info(r.__str__())


if __name__ == "__main__":
    '''
    PS  C:\\Users\\Veronika\\PycharmProjects\\pythonProject\\homework10"
    '''

    create_log("C:\\Users\\Veronika\\PycharmProjects\\pythonProject\\homework10")

