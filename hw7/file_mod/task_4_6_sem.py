import os
import random as rnd
import string

"""Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.

Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.

Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""


def inner_func(extension: str, directory: str = '', min_size: int = 6, max_size: int = 30,
               min_count: int = 256, max_count: int = 4096, file_count: int = 42):
    letters = string.ascii_lowercase

    if directory:
        if not os.path.isdir(directory):
            os.mkdir(directory)

    for _ in range(file_count):
        name_size = rnd.randint(min_size, max_size)
        name = rnd.choices(letters, k=name_size)
        name = ''.join(name)

        if os.path.isfile(os.path.join(directory, name + extension)):
            x = 1
            while os.path.isfile(os.path.join(directory, name + f'_{x}' + extension)):
                x += 1
            file_name = name + f'_{x}' + extension
        else:
            file_name = ''.join(name) + extension

        rnd_size = rnd.randint(min_count, max_count)
        data = rnd.randbytes(rnd_size)

        with open(os.path.join(directory, file_name), 'wb') as file:
            file.write(data)


def func_new_files(extensions: tuple, directory: str = '', file_count: int = 1):
    for _ in range(file_count):
        extension = rnd.choice(extensions)
        inner_func(extension, directory=directory, file_count=1)


if __name__ == '__main__':
    func_new_files(('.txt', '.bmp', '.jpg', '.mp3', '.doc', '.docx',
                    '.json', '.xyz', '.sos'), 'some_trash', 35)
