"""✔ Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.

Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""
from os import close
import datetime as dt


class ATM:
    def __init__(self):
        self._balance = 0
        self.count = 0
        self.id = id(self)
        self.history = []

    # пополнение баланса счета
    def top_up_balance(self, summ):
        if self._balance > 5_000_000:
            self.history.append(f"tax_rich 10% +{self._balance * 0.1:.2f}")
            self._balance *= 0.9
        if summ % 50:
            print(f'{dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S-%f")} Ошибка! Введите сумму пополнения, кратную 50 у.е')
        else:
            self._balance += summ
            self.history.append(f"up +{summ}")
            self.count += 1
        if not self.count % 3 and self.count > 0:
            self._balance *= 1.03
            self.history.append(f"interest for 3d transaction +{self._balance * 0.03:.2f}")
        print(f'{dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S-%f")} Баланс счета {self._balance:.2f} у.е')

        self.write_to_file()

    # снятие денег со счета
    def withdraw(self, summ):
        if self._balance > 5_000_000:
            self.history.append(f"tax_rich 10% -{self._balance * 0.1:.2f}")
            self._balance *= 0.9
        if summ % 50:
            print(f'{dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S-%f")} Ошибка! Введите сумму снятия, кратную 50 у.е')
        elif summ > self._balance:
            print(f'{dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S-%f")} Ошибка! На счете недостаточно средств')
        else:
            self._balance -= summ
            self.history.append(f"withdraw -{summ}")
            if summ * 1.5 / 100 < 30:
                fee = 30
            elif summ * 1.5 / 100 > 600:
                fee = 600
            else:
                fee = summ * 1.5 / 100
            self._balance -= fee
            self.history.append(f"withdraw fee -{fee}")
            self.count += 1
        if not self.count % 3 and self.count > 0:
            self._balance *= 1.03
            self.history.append(f"interest for 3d transaction +{self._balance * 0.03:.2f}")
        print(f'{dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S-%f")} Баланс счета {self._balance:.2f} у.е.')
        self.write_to_file()
    def write_to_file(self):
        with open(f'account {self.id}.txt', 'a', encoding='UTF-8') as f:
            f.write(f'{dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S-%f")} Баланс счета {self._balance:.2f} у.е.\n')
    def exit(self):
        self.write_to_file()
        close(0)


account1 = ATM()
account1.withdraw(50) #неудачная операция снятия, на счете 0 у.е.
account1.top_up_balance(63) #неудачная операция пополнения, сумма не кратна 50 у.е.
account1.top_up_balance(10_000) #операция №1 пополнение на 10_000 у.е.
account1.withdraw(153) #неудачная операция снятия, сумма не кратна 50 у.е.
account1.withdraw(1_000) #операция №2 снятие 1_000 у.е. Результат 10_000 - 1_000 - 30(т.к. 1.5% = 15) = 8_970 у.е.
account1.top_up_balance(1_000) #операция №3 пополнение 1_000 у.е. Результат 8_970 + 1_000 + 3% (8_970 + 1_000) = 10_269.10 у.е.
account1.top_up_balance(5_000_000) #операция №4 пополнение 5_000_000 у.е. Результат 10_269.10 + 5_000_000 = 5_010_269.10 у.е.
account1.withdraw(303) #неудачная операция снятия, сумма не кратна 50 у.е. Т.к. баланс > 5 млн.
# то применяется налог 10% на богадство даже в случае неудачного завершения операции. Баланс 5_010_269.10 * 0.9 = 4_509_242.19 у.е.
account1.withdraw(1_000_000) #операция №5 снятие 1_000_000 у.е. Результат 4_509_242.19 - 1_000_000 - 600(т.к. 1.5% = 15_000) = 3_508_642.19 у.е.
account1.withdraw(1_000_000) #операция №6 снятие 1_000_000 у.е. Результат 3_508_642.19 - 1_000_000 - 600(т.к. 1.5% = 15_000) = 2_508_042.19 у.е.  + 3% (за 6-ю операцию) = 2_583_283.46 у.е.
account1.withdraw(1_000_000) #операция №7 снятие 1_000_000 у.е. Результат 2_583_283.46 - 1_000_000 - 600(т.к. 1.5% = 15_000) = 1_582_683.46 у.е.
print(account1.count) #количество успешных операций пополнения и снятия
print(*account1.history, sep='\n') #история движения денежных средств
account1.exit()
