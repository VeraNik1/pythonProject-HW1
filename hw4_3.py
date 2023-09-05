"""✔ Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление"""

def make_dictionary(**kwargs):
    result = dict()
    for k, v in kwargs.items():
        if type(v) in [int, float, str, tuple, frozenset]:
            result[v] = k
        else:
            result[str(v)] = k
    return result

result = make_dictionary(name='Вася', age=3, weight=12.5, friends=['катя', 'миша'],
                         parents=('mom', 'dad'), toys=frozenset({'cat','duck'}))
print(result)
