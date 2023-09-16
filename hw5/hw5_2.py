"""Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""
def prime_number_generator(N):
    for num in range(2, N + 1):
        for i in range(2, num // 2 + 3):
            if num != i:
                if num % i == 0:
                    break
            else:
                yield num
            if i == num // 2:
                yield num

x = prime_number_generator(130)
y = prime_number_generator(11)
z = prime_number_generator(100) #25 простых чисел в интервале от 1 до 100
print(*x)
print(*y)
print(len(list(z)))
print(*prime_number_generator(1000))
print(len(tuple(prime_number_generator(1000)))) #168 простых чисел в интервале от 1 до 1000 пишут в просторах тырнета