"""Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции."""


import json
import os
from typing import Callable
from functools import wraps


def logger_json(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        data = {}
        if os.path.isfile(file_name) and os.path.exists(file_name):
            with open(file_name, 'r', encoding='UTF-8') as file:
                data = json.load(file)
        result = func(*args, **kwargs)
        data[result] = {'args': args, 'kwargs': kwargs}
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return result

    return wrapper


@logger_json
def summarize(a, b):
    return a + b


if __name__ == '__main__':
    print(summarize(1, 2))
    print(summarize(b=2, a=5))
    print(summarize(6, b=2))
