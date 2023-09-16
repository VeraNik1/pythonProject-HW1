import random
def try_to_guess() -> int:
    func_dict = {'Зимой и летом одним цветом': ['ёлка', 'ель', 'ёлочка'],
                 'Ни лает, ни кусает, в дом не пускает': ['замок', 'замочек'],
                 'Висит груша нельзя скушать': ['лампочка', 'лампа']}
    while func_dict:
        key = random.choice(func_dict.keys())
        yield func_dict.pop(key)


def my_game(cnt: int) -> int:
    temp_cnt = 1
    riddle, ans = try_to_guess()
    while temp_cnt <= cnt:

        answer = input('Введите ответ').lower()
        if answer in ans:
            return temp_cnt
        temp_cnt += 1
    return 0


