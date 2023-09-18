# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from file_mod import (number_to_file, write_names_to_file, combining_func, func_new_files,
                      sort_file_function, change_file_name)

number_to_file('test_1.txt', 10)
write_names_to_file('test_2.txt', 6)
combining_func('test_1.txt', 'test_2.txt', 'test_3.txt')
func_new_files(('.txt', '.bmp', '.jpg'), 'x_files', 22)
sort_file_function('x_files')
change_file_name(3, '.txt', [1, 3], '_VERA_', 'x_files/documents')