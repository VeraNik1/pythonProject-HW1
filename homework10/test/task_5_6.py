# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


# Вынесите общие свойства и методы классов в класс Животное.
# 📌Остальные классы наследуйте от него.
# 📌Убедитесь, что в созданные ранее классы внесены правки.


class Animal:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.voice = None

    def get_voice(self):
        return self.voice


class Dog(Animal):

    def __init__(self, name: str, age: int, voice='auuuuu'):
        super().__init__(name, age)
        self.voice = voice


class Cat(Animal):

    def __init__(self, name: str, age: int, voice='mrrr'):
        super().__init__(name, age)
        self.voice = voice


class Bird(Animal):

    def __init__(self, name: str, age: int, voice='twitwi'):
        super().__init__(name, age)
        self.voice = voice


if __name__ == '__main__':
    dog_1 = Dog('Oleg', 3, 'wooof')
    cat_1 = Cat('Fudge', 5, 'meow')
    bird_1 = Bird('Popka', 2, 'popka_khoroshiy')

    for pet in [dog_1, cat_1, bird_1]:
        print(f'{pet.name} {pet.get_voice()}')
