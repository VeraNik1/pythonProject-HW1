"""Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите
функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра."""


class Triangle:

    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def triangle_check(self):
        if self.side_a <= 0 or self.side_b <= 0 or self.side_c <= 0:
            raise ValueError("Значения сторон треугольника не могут быть <= 0")
        if (self.side_a + self.side_b > self.side_c and self.side_a + self.side_c > self.side_b
                and self.side_b + self.side_c > self.side_a):
            if self.side_a == self.side_b == self.side_c:
                return f'Треугольник со сторонами {self.side_a}-{self.side_b}-{self.side_c} равносторонний'
            elif self.side_a == self.side_b or self.side_a == self.side_c or self.side_b == self.side_c:
                return f'Треугольник со сторонами {self.side_a}-{self.side_b}-{self.side_c} равнобедренный'
            else:
                return f'Треугольник со сторонами {self.side_a}-{self.side_b}-{self.side_c} разносторонний, как ты'
        else:
            raise ValueError(f'Треугольника со сторонами {self.side_a}-{self.side_b}-{self.side_c} не существует')


if __name__ == '__main__':
    obj_1 = Triangle(2, 2, 2)
    print(obj_1.triangle_check)
    obj_2 = Triangle(2, 3, 3)
    print(obj_2.triangle_check)
    obj_3 = Triangle(2, 3, 4)
    print(obj_3.triangle_check)
    # obj_4 = Triangle(1, 10, 3)
    # print(obj_4.triangle_check) # ValueError
    obj_5 = Triangle(1, 6, -2)
    print(obj_5.triangle_check)  # ValueError
