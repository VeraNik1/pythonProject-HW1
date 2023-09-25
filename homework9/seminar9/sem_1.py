"""
1. 📌Создайте функцию-замыкание, которая запрашивает два целых числа: ○ от 1 до 100 для загадывания, ○
от 1 до 10 для количества попыток
📌Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

."""

import random as rnd
from typing import Callable


def outer():
    a = rnd.randint(1, 100)
    b = rnd.randint(1, 10)

    def guess_number():
        nonlocal a, b
        while b:
            print(f'У тебя осталось попыток: {b}')
            user_choice = int(input('Введите свое число от 1 до 100: '))
            if user_choice < a:
                print(f'{user_choice} меньше загаданного')
            elif user_choice > a:
                print(f'{user_choice} больше загаданного')
            else:
                print(f'Ты угдал число {user_choice}')
                break
            b -= 1
        else:
            print(f'Ты не угадал число {a}')

    return guess_number()


if __name__ == '__main__':
    outer()
