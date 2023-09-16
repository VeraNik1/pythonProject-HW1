'''
a = 3
b = 4.6
c = 'string'
d = True


print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(type('a'))
print(True + 1)
print(type(None))

"""Создайте в переменной data список значений
 разных типов перечислив их через запятую внутри
  квадратных скобок. Для каждого элемента в цикле 
  выведите: 
  ✔порядковый номер начиная с единицы 
  ✔значение 
  ✔адрес в памяти 
  ✔размер в памяти 
  ✔хэш объекта 
  ✔результат проверки на целое число только если он положительный 
  ✔результат проверки на строку только если он положительный 
  Добавьте в список повторяющиеся элементы и сравните на результаты."""

array = [1, 2.2, 'string', True, 1, 4.5, False, True, 'string']
for i in range(len(array)):
    print('Порядковый номер: ', i + 1)
    print('Значение', array[i])
    print('адрес в памяти', id(array[i]))
    print('размер в памяти', array[i].__sizeof__())
    print('хэш объекта', hash(array[i]))
    if isinstance(array[i], int | float):
        print('Это число')
    if isinstance(array[i], str):
        print('Это строка')
    print('=' * 20)


a = 5
b = a
b += 1
print(a)

a = ['5' for _ in range(20)]
for i in a:
    print(id(i))'''


"""✔Напишите программу, которая получает целое число и возвращает его двоичное,
 восьмеричное строковое представление. 
 ✔Функции bin и oct используйте для проверки своего результата, а не для решения. 
 Дополнительно: 
 ✔Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления 
 ✔Избегайте магических чисел 
 ✔Добавьте аннотацию типов где это возможно"""

a = 350
n = a
result_bin = ''
while n > 0:
    result_bin = str(n % 2) + result_bin
    n //= 2
result_bin = '0b' + result_bin

print(result_bin)
print(bin(a))
print(result_bin == bin(a))

b = 350
m = b
result_oct = ''
while m > 0:
    result_oct = str(m % 8) + result_oct
    m //= 8
result_oct = '0o' + result_oct
print(result_oct)
print(oct(b))
print(result_oct == oct(b))

"""✔Напишите программу, которая вычисляет площадь круга и 
длину окружности по введённому диаметру. 
✔Диаметр не превышает 1000 у.е. 
✔Точность вычислений должна составлять не менее 42 знаков после запятой."""
import decimal
import math
decimal.getcontext().prec = 42
d = decimal.Decimal(input("Введите диаметр окружности: "))
if d > 1000:
    print('Слишком большое число')
else:
    print(f"длина окружности {decimal.Decimal(math.pi) * d}")
    print(f"площадь круга {decimal.Decimal(math.pi) * d ** 2 / 4}")


"""✔Напишите программу, которая решает квадратные уравнения даже
 если дискриминант отрицательный. 
✔Используйте комплексные числа для извлечения квадратного корня."""

a = 1
b = -10
c = 15

d = complex(b**2 - 4*a*c, 0)
x1 = (-b + d**0.5)/(2*a)
x2 = (-b - d**0.5)/(2*a)
print(d, x1, x2)
