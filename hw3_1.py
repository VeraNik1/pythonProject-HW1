"""Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей."""

camping_data = {'Олег': ('термос', 'палатка', 'спальный мешок', 'еда', 'спички'),
                'Василий': ('термос', 'палатка', 'спальный мешок', 'еда', 'презервативы', 'кастрюля'),
                'Паша': ('термос', 'палатка', 'спальный мешок', 'еда', 'спички', 'средство от комаров'),
                'Костя': ('термос', 'палатка', 'спальный мешок', 'презервативы', 'кастрюля', 'лопата')
                }
#множество вещей у всех друзей
items_list = set()

for item in camping_data.values():
    items_list = items_list | set(item)
print(items_list)

#Какие вещи взяли все три друга (все друзья)
common_items = items_list
for item in camping_data.values():
    common_items = common_items & (set(item))
# common_items = set() # для проверки если нет общего пересечения
print(('Друзья не брали одинаковых вещей', f"Все друзья взяли: {common_items}")[len(common_items) > 0])

#Какие вещи уникальны, есть только у одного друга
for k, v in camping_data.items():
    result = set(v)
    for key, value in camping_data.items():
        if key != k:
            result -= set(value)
    if result:
        print(f'{k} взял уникальную вещь/и - {result}')

#Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
for k, v in camping_data.items():
    result = set(v)
    common_for_others = items_list
    for key, value in camping_data.items():
        if key != k:
            common_for_others  = common_for_others & set(value)
    result = common_for_others - result
    if result:
        print(f'Только {k} не взял - {result}, остальные взяли')

#Проверка через словари
items_statistic = {}
for item in items_list:
    for k, v in camping_data.items():
        if item in v:
            items_statistic[item] = items_statistic.get(item, ()) + (k,)

print(items_statistic)

#Какие вещи взяли все три друга (все друзья)
print('Все друзья взяли: ', end = ' ')
print(*filter(lambda x: len(items_statistic[x]) == len(camping_data), items_statistic), sep=',')

#Какие вещи уникальны, есть только у одного друга

for k, v in items_statistic.items():
    if len(v) == 1:
        print(f'{v[0]} взял уникальную вещь/и - {k}')


#Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
for k, v in items_statistic.items():
    if len(v) == len(camping_data) - 1:
        print(f'Только {set(camping_data) - set(v)} не взял - {k}, остальные взяли')