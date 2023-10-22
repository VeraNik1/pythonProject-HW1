"""
Задание №3
Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class BaseExceptions(Exception):
    pass


class LevelError(BaseExceptions):
    pass


class AccessError(BaseExceptions):
    pass


class InvalidNameError(BaseExceptions):
    pass


class InvalidLevelError(BaseExceptions):
    pass


class InvalidIdError(BaseExceptions):
    pass



def fun(num):
    if num < 2:
        raise AccessError

    elif num > 5:
        raise LevelError
    else:
        print('все ок')


if __name__ == '__main__':
    # raise LevelError(4)
    fun(2)
