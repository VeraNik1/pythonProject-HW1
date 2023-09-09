"""✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""

import re
import os
def path_name_ext_re(text):
    m = re.match(r"(^.+[\\/])(\w+)\.([a-zA-Z]{2,}$)", text)
    return m.group(1), m.group(2), m.group(3)


def path_name_ext_os(path):
    filepath, file_extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, file_extension)



print(path_name_ext_re('C:\\Users\Veronika\Desktop\\bootcamp.csproj'))
print(path_name_ext_re('C:\\Users\Veronika\PycharmProjects\pythonProject\\venv\Scripts\python.exe'))
print(path_name_ext_re("D:/Autotests/My first project/Studying project/Tests/Tests results/results.txt"))

print(path_name_ext_os('C:\\Users\Veronika\Desktop\\bootcamp.csproj'))
print(path_name_ext_os('C:\\Users\Veronika\PycharmProjects\pythonProject\\venv\Scripts\python.exe'))
print(path_name_ext_os("D:/Autotests/My first project/Studying project/Tests/Tests results/results.txt"))