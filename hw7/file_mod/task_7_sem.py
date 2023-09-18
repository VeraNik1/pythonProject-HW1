import os
import random as rnd
import string
from pathlib import Path

"""Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""

AUDIO_DIR = 'music'
IMAGES_DIR = 'images'
TEXT_DIR = 'documents'
AUDIO_EXTENSION = ('.mp3',)
IMAGES_EXTENSION = ('.jpg', '.bmp')
TEXT_EXTENSION = ('.txt', '.doc', '.docx')


def check_directory(current_dir: str):
    list_dir = [obj.name for obj in current_dir.iterdir() if obj.is_dir()]
    if AUDIO_DIR not in list_dir:
        Path.mkdir(current_dir / AUDIO_DIR)
    if IMAGES_DIR not in list_dir:
        Path.mkdir(current_dir / IMAGES_DIR)
    if TEXT_DIR not in list_dir:
        Path.mkdir(current_dir / TEXT_DIR)


def sort_file_function(dir_name):
    current_directory = Path.cwd()
    dir_path = current_directory / dir_name
    check_directory(dir_path)
    for obj in dir_path.iterdir():
        if obj.suffix in TEXT_EXTENSION:
            obj.replace(dir_path / TEXT_DIR / obj.name)
        elif obj.suffix in AUDIO_EXTENSION:
            obj.replace(dir_path / AUDIO_DIR / obj.name)
        elif obj.suffix in IMAGES_EXTENSION:
            obj.replace(dir_path / IMAGES_DIR / obj.name)


if __name__ == '__main__':
    sort_file_function('some_trash')
