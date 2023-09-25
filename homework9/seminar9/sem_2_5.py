"""2. 📌Дорабатываем задачу 1
📌Превратите внешнюю функцию в декоратор.
📌Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
📌Если не входят, вызывать функцию со случайными числами из диапазонов"""

import random as rnd
import sem_4 as s
import sem_3 as d
from functools import wraps


def deco(func):
    @wraps(func)
    def inner(*args):
        a, b, *_ = args
        if a not in range(1, 101):
            a = rnd.randint(1, 100)
            print(f'Число не попало в заданный диапазон! Изменено на {a}')
        if b not in range(1, 11):
            b = rnd.randint(1, 10)
            print(f'Число не попало в заданный диапазон! Изменено на {b}')
        func(a, b)

    return inner


@s.restarting_func(3)
@deco
@d.logger_json
def guess_number(a: int, b: int):
    print(f'Новая игра\n')
    while b:
        print(f'У тебя осталось попыток: {b}\n')
        try:
            user_choice = int(input('Введите свое число от 1 до 100: '))
            if user_choice > 100 or user_choice < 1:
                print('Необходимо ввести число в диапазоне от 1 до 100\n')
                continue
        except:
            print('Введено не число\n')
            continue

        if user_choice < a:
            print(f'{user_choice} меньше загаданного')
        elif user_choice > a:
            print(f'{user_choice} больше загаданного')
        else:
            print(f'Ты угадал число {user_choice}\n')
            return str(user_choice)
        b -= 1
    else:
        print(f'Ты не угадал число {a}')
        return f'Ты не угадал число {a}'


if __name__ == '__main__':
    guess_number(200, 100, 50, 88, "asasa")
