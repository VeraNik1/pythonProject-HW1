"""Задание №7
✔ Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата."""
import decimal

number = int(input("Введите натуральное число >>> "))
m = number

BASE = 16
data_hex = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

result_hex = ''
while m > 0:
    if m % BASE in data_hex:
        result_hex = data_hex[m % BASE] + result_hex
    else:
        result_hex = str(m % BASE) + result_hex
    m //= BASE
result_hex = '0x' + result_hex

print("Задание 1")
print(result_hex)
print(hex(number))  # проверка
print(result_hex == hex(number))  # проверка

"""✔ Напишите программу, которая принимает две строки
вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму
и *произведение дробей. Для проверки своего
кода используйте модуль fractions."""

import fractions
from functools import singledispatchmethod


class DecimalMy():
    @singledispatchmethod
    def __init__(self, arg):

        raise TypeError('Аргумент переданного типа не поддерживается')

    # создание экземляра класса из строки
    @__init__.register(str)
    def fraction_from_string(self, arg):
        try:
            self.numerator, self.denominator = map(int, arg.replace(" ", "").split('/'))
            if self.denominator == 0 or self.numerator == 0:
                raise ValueError('Значения числителя и знаменателя не должны быть равны 0')
        except:
            raise TypeError('Некорректный тип строки')

    # создание экземляра класса из int
    @__init__.register(int)
    def fraction_from_string(self, arg1, arg2 = 1):
        self.numerator, self.denominator = arg1, arg2
        if self.denominator == 0 or self.numerator == 0:
            raise ValueError('Значения числителя и знаменателя не должны быть равны 0')

    # создание экземляра класса из строки длиной 2
    @__init__.register(tuple)
    @__init__.register(list)
    def fraction_from_string(self, arg):
        if len(arg) != 2:
            raise TypeError('Некорректный длина массива/кортежа, должно быть 2 числа')
        try:
            self.numerator, self.denominator = map(int, arg)
            if self.denominator == 0 or self.numerator == 0:
                raise ValueError('Значения числителя и знаменателя не должны быть равны 0')
        except:
            raise TypeError('Некорректные значения в списке/кортеже')

    # наибольший общий делитель
    @staticmethod
    def gcd(num, denum):
        temp = 1
        if num < denum:
            num, denum = denum, num
        while temp != 0:
            temp = num % denum
            num = denum
            denum = temp
        return num

    # сокращение дроби с учетом наибольшего общего делителя
    @staticmethod
    def _make_correct_decimal(num, denum):
        gcd = DecimalMy.gcd(num, denum)
        return num // gcd, denum // gcd

    # вывод дроби на печать с выделением целой части (при наличии)
    def __str__(self):
        if self.numerator % self.denominator == 0:
            return str(self.numerator // self.denominator)
        self.numerator, self.denominator = DecimalMy._make_correct_decimal(self.numerator, self.denominator)
        if abs(self.numerator) >= abs(self.denominator):
            int_part = abs(self.numerator // self.denominator)
            if self.numerator * self.denominator > 0:
                return f"{int_part} {abs(self.numerator % self.denominator)}/{abs(self.denominator)}"
            return f"-{int_part} {abs(self.numerator % self.denominator)}/{abs(self.denominator)}"
        if self.numerator * self.denominator > 0:
            return f"{abs(self.numerator)}/{abs(self.denominator)}"
        return f"-{abs(self.numerator)}/{abs(self.denominator)}"
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    # сложение дробей
    def __add__(self, other):
        res_num = self.numerator * other.denominator + other.numerator * self.denominator
        res_denum = other.denominator * self.denominator
        return DecimalMy((res_num, res_denum))

    # вычитание дробей
    def __sub__(self, other):
        res_num = self.numerator * other.denominator - other.numerator * self.denominator
        res_denum = other.denominator * self.denominator
        return DecimalMy((res_num, res_denum))

    # перемножение дробей
    def __mul__(self, other):
        res_num = self.numerator * other.numerator
        res_denum = other.denominator * self.denominator
        return DecimalMy((res_num, res_denum))

    # деление дробей
    def __truediv__(self, other):
        res_num = self.numerator * other.denominator
        res_denum = other.numerator * self.denominator
        return DecimalMy((res_num, res_denum))

print()
print("="*50)
print("Задание 2")

# Проверка
str_a = '10/8'
a = DecimalMy(str_a)
print("1. ", a)
print("2. ", repr(a))
print("3. ", fractions.Fraction(10, 8))

b = DecimalMy('16/8')
print(fractions.Fraction(16, 8))
print("4. ", b)
print("5. ", a + b)
print("6. ", b - a)
print("7. ", a / b)
print("8. ", a * b)

d = DecimalMy('-6/13')
print("10. ", fractions.Fraction(-6, 13))
print("11. ", d)
print("12. ", a + d)
print("13. ", b - d)
print("14. ", a / d)
print("15. ", repr(a / d))
print("16. ", fractions.Fraction(10, 8) / fractions.Fraction(-6, 13))
print("17. ", a * d)
print("18. ", fractions.Fraction(10, 8) / fractions.Fraction(-6, 13))


g = DecimalMy((7, 5))
print(g)

