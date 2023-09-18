import random as rnd
from string import ascii_lowercase

LETTER = ascii_lowercase
VOWELS = 'aeiouy'


def generate_name() -> str:
    size = rnd.randint(4, 7)
    name = rnd.sample(LETTER, size - 1)
    name.append(rnd.choice(VOWELS))
    rnd.shuffle(name)
    name = ''.join(name).title()
    return name


def write_names_to_file(filename: str, count: int):
    names = []
    with open(filename, 'a', encoding='UTF-8') as file:
        for _ in range(count):
            names.append(generate_name())
        file.write('\n'.join(names))


if __name__ == '__main__':
    write_names_to_file('task_2_sem.txt', 10)
