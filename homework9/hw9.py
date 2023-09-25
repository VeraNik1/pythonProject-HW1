"""Напишите следующие функции:
    ○ Нахождение корней квадратного уравнения
    ○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
    ○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
    ○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса"""
import csv
import json
import os
from typing import Callable
from random import randint as r

UPPER_LIMIT = 222
PATH_FILE = 'numbers.csv'


def logger_json(func: Callable) -> Callable:
    """
    Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
    {параметры: результат}
    """

    def wrapper(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        data = {}
        if os.path.isfile(file_name) and os.path.exists(file_name):
            with open(file_name, 'r', encoding='UTF-8') as file:
                data = json.load(file)
        result = func(*args, **kwargs)
        first_step, second_step = '', ''
        if args:
            first_step = ' '.join(list(map(str, args)))
        if kwargs:
            second_step = [f'{k}-{v}' for k, v in kwargs.items()]
        data[first_step + second_step] = result
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return result

    return wrapper


def start_function(func: Callable) -> Callable:
    """
    декоратор запускающий функцию нахождения корней квадратного
    уравнения с каждой тройкой чисел из csv файла.
    """
    def inner(*args, **kwargs):
        if os.path.isfile(PATH_FILE) and os.path.exists(PATH_FILE):
            with open(PATH_FILE, 'r', encoding='UTF-8') as file:
                data = file.readlines()
            for elem in data:
                a, b, c = map(int, elem.strip().split(','))
                func(a, b, c)
        return func(*args, **kwargs)

    return inner


@start_function
@logger_json
def quadratic_equation(a=1, b=1, c=1):
    """
    функция нахождения корней квадратного уравнения
    """
    if a == 0:
        return "Уравнение не является квадратным а = 0"
    discr = b * b - 4 * a * c

    if discr > 0:
        return (-b + discr ** 0.5) / (2 * a), (-b - discr ** 0.5) / (2 * a)
    elif discr == 0:
        return (-b / (2 * a),)
    else:
        return 'Не имеет действительных корней'


def csv_file_generator(path: str = PATH_FILE):
    """
    Генерация csv файла с тремя случайными числами в каждой строке
    """
    data_list = [(r(-20, 20) for _ in range(3)) for _ in range(UPPER_LIMIT)]
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)


csv_file_generator()
quadratic_equation()
