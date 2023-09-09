"""Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
"""

names = ["Vasya", "Petya", "Oleg"]
salary = [150_000, 300_000, 250_000]
bonus = ["10.2%", "12.4%", "21.6%"]


result = {n: s * float(b[:-1]) / 100 for n, s, b in zip(names, salary, bonus)}

print(result)
