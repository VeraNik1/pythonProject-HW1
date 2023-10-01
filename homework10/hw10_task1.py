# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


from task_5_6 import Dog, Cat, Bird


class Farm:
    type_list = ['dog', 'cat', 'bird']

    def __init__(self, type_animal, name: str, age: int, voice=None):
        self.type_animal = self.__setup_animal_type(type_animal)
        self.voice = voice
        if not self.voice:
            self.params = (name, age)
        else:
            self.params = (name, age, voice)

    def get_animal(self):
        if self.type_animal == 'dog':
            return Dog(*self.params)
        if self.type_animal == 'cat':
            return Cat(*self.params)
        if self.type_animal == 'bird':
            return Bird(*self.params)

    def __setup_animal_type(self, type_animal):
        if type_animal in self.type_list:
            return type_animal
        else:
            raise ValueError


if __name__ == '__main__':
    pet_01 = Farm('dog', 'Steven', 2, 'wtfwooof').get_animal()
    pet_02 = Farm('cat', 'Betty', 3).get_animal()

    print(type(pet_01))
    print(f'{pet_01.name} {pet_01.get_voice()}')
    print(type(pet_02))
    print(f'{pet_02.name} {pet_02.get_voice()}')
