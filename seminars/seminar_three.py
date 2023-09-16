"""✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа."""


"""example = (25, 78.3, [1, 2, 3], ('asdadad', 'sdkjskajdl'), 33,
           'hasgdjasgj', 'gdjsfgjsafjag', 12.6, [3, 8, 19, 22],
           {3, 7}, {'a': 1, 'b': 4}, dict(), 45.3, [0, 0, 0], {'a', 'b', 'c'})

result = dict()
for item in example:
    if type(item) in result:
        result[type(item)].append(item)
    else:
        result[type(item)] = [item]

print(result)

result1 = dict()
for item in example:
    result1.setdefault(type(item), [])
    result1[type(item)].append(item)
print(*result1)"""

"""✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды."""

"""example = [1, 7, 8, 10, 13, 13, 13, 14, 1, 1, 2, 3, 7, 3, 10, 10, 1, 13]

result = list(set((filter(lambda x: example.count(x) % 2, example))))
print(result)

result1 = []
for item in example:
    if example.count(item) % 2 and item not in result1:
        result1.append(item)
print(result1)

example2 = [1, 7, 8, 10, 13, 13, 13, 14, 1, 1, 2, 3, 7, 3, 10, 10, 1, 13]
i = 0
while i < len(example2):
    if example2.count(example2[i]) >= 2:
        item = example2[i]
        example2.remove(item)
        example2.remove(item)
    else:
        i += 1

print(example2)"""

"""Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки."""

'''text = sorted(input("Введите строку>>>> ").split())
max_len = len(max(text, key=len))
for k, v in enumerate(text, 1):
    print(f"{k}.{' '*(max_len - len(v))} {v}")'''

"""✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях."""

text = input("Введите строку>>>> ")
result = dict()
for item in text:
    result[item] = result.get(item, 0) + 1
print(result)