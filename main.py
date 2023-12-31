# Homework №1
'''Выведите в консоль таблицу
умножения от 2х2 до 9х10 как на школьной тетрадке.'''


def multiply(i, j):
    return "{0} X {1:2} = {2:2}".format(i, j, j * i)


text = 'ТАБЛИЦА УМНОЖЕНИЯ'
print()
print(text.center(56, " "))
print()
for i in range(1, 11):
    print(multiply(2, i), multiply(3, i), multiply(4, i), multiply(5, i), sep='    ')

print()
for i in range(1, 11):
    print(multiply(6, i), multiply(7, i), multiply(8, i), multiply(9, i), sep='    ')

# Homework №2
''' Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.'''


def triangle_check(a, b, c):
    if a <= 0 or b <= 0 or c <=0:
        print("Значения сторон треугольника не могут быть <= 0")
        return
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print(f'Треугольник со сторонами {a}-{b}-{c} равносторонний')
        elif a == b or a == c or b == c:
            print(f'Треугольник со сторонами {a}-{b}-{c} равнобедренный')
        else:
            print(f'Треугольник со сторонами {a}-{b}-{c} разносторонний, как ты')
    else:
        print(f'Треугольника со сторонами {a}-{b}-{c} не существует')


print()

print("Введите длины сторон треугольника")

a, b, c = int(input("сторона a: >>> ")), int(input("сторона b: >>> ")), int(input("сторона c: >>> "))
triangle_check(a, b, c)

# Homework №3
'''Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.'''


def prime_number_check(num):
    if num < 0 or num > 10 ** 5:
        print(f"Число не входит в диапазон проверяемых, нужно ввести число от 0 до  100 тысяч")
        return
    elif num in [0, 1]:
        print(f"Число {num} не является ни простым, ни составным")
        return
    for i in range(2, num // 2 + 1):
        if num != i:
            if num % i == 0:
                print(f"Число {num} является составным")
                return
    print(f"Число {num} является простым")


print()

print("Ввести число от 0 до  100 000:")
number = int(input(">>> "))
prime_number_check(number)

print()

# Homework №4
'''Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

from random import randint

num = randint(0, 1000)
#print(f"Компьтер загадал {num}, но ты не смотри сюда, используй интуицию")
print("Программа загадала число от 0 до 1000 и у тебя 10 попыток, чтобы угадать)")
for i in range(10):
    chance = int(input(f"{i + 1}-я попытка! >>>  "))
    if chance == num:
        print(f"Поздравляю, вы угадали число {num} с {i + 1}-й попытки")
        break
    elif chance > num:
        print(f"Вы должны ввести число меньше, чем {chance}")
    else:
        print(f"Вы должны ввести число больше, чем {chance}")
if chance != num:
    print(f"Сожалею, вы не угадали число {num} за 10 попыток")

# Homework №4.1
"""Пользователь задумывает число
Программа пытается угадать число за 10 попыток
компьтер выводит свое предположение и запрашивает у пользователя информацию:

Если компьтер угадал число введите =
Если Ваше число больше, введите >
Если Ваше число меньше, введите <

"""

from random import randint
print()
print("Задумайте число от 0 до 1000, компьютер попытается угадать число с 10-ти попыток")

left = 0
right = 1000
current = (left + right) // 2
answer = None
counter = 0
while answer != '=' and counter < 10:
    if right < left:
        print("Похоже Вы забыли, какое число загадали, либо что-то перепутали). Я так не играю!")
        counter = 0
        break
    print(f"Попытка №{counter + 1}: Вы загадали {current}?")
    answer = input("Если компьтер угадал число введите = \nЕсли Ваше число больше, введите >\nЕсли Ваше "
                   "число меньше, введите <\n>>>>  ")
    if answer == '=':
        print(f"Я угадал c {counter + 1}-й попытки!")
        counter = 0
        break
    elif answer == '>':
        left = current + 1
        counter += 1
    elif answer == '<':
        right = current - 1
        counter += 1
    else:
        print('Повторите ввод (>, <, =)!')
    current = (left + right) // 2

if counter:
    print("Я не угадал число( за 10 попыток")
