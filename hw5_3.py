"""✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""

import re
def path_name_ext(text):
    m = re.match(r"(^.+[\\/])(\w+)\.([a-zA-Z]{2,}$)", text)
    return m.group(1), m.group(2), m.group(3)

print(path_name_ext('C:\\Users\Veronika\Desktop\\bootcamp.csproj'))
print(path_name_ext('C:\\Users\Veronika\PycharmProjects\pythonProject\\venv\Scripts\python.exe'))
print(path_name_ext("D:/Autotests/My first project/Studying project/Tests/Tests results/results.txt"))