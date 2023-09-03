"""Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
Верните все возможные варианты комплектации рюкзака"""


items = {'носки': 0.2,
         'спальный мешок': 1.5,
         'кружка': 0.3,
         'фонарь': 1,
         'хлеб': 1.2,
         'нож': 0.2,
         'топор': 2.5,
         'книга': 0.5,
         'веревка': 0.4,
         'котелок': 1.8,
         'вода': 3.5,
         'аптечка': 1,
         'палатка': 10,
         'шампура': 1.5,
         'мангал': 2.4,
         'мясо': 2,
         'складной стул': 4,
         'миска': 1,
         'жидкость для розжига': 1.5,
         'резиновая лодка': 6,
         'компрессор': 2.5,
         'аккумулятор': 4.8}

max_weight = float(input("Введите максимальный вес рюкзака >>>>  "))


#Достаточно вернуть один допустимый вариант.
def backpack(items, max_weight):
    possible_items = []
    backpack_weight = 0
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            backpack_weight += weight
            max_weight -= weight
    return possible_items, backpack_weight


result = backpack(items, max_weight)
print(*result[0], f'- общий вес рюкзака - {result[1]:4}')

# Верните все возможные варианты комплектации рюкзака
def find_all_combinations(items, max_weight):
    result = []
    #сортирую список в порядке убывания массы
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    #функция для поиска комбинаций(рекурсия)

    def find_combinations_recursively(current_weight, current_combination, remaining_items):

        # условие, когда комплектация рюкзака найдена

        if current_weight <= max_weight:
            result.append(current_combination)

        for i in range(len(remaining_items)):
            new_combination = current_combination + [remaining_items[i]]
            new_weight = current_weight + items[remaining_items[i]]
            new_remaining = remaining_items[i+1:]
            find_combinations_recursively(new_weight, new_combination, new_remaining)


    find_combinations_recursively(0, [], sorted_items)
    return result

all_combinations = find_all_combinations(items, 4)[1:]
for combination in all_combinations:
    print(*combination, f'- общий вес рюкзака - {sum(items[k] for k in items if k in combination)}')

print(f'Всего найдено - {len(all_combinations)} комбинаций')

print(len(set(map(frozenset, all_combinations)))) #проверка нет ли одинаковых комбинаций