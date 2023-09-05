"""Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце."""

def change_var(var, vars_data = vars()):
    vars_data_temp = vars_data.copy()
    for var_name in vars_data_temp:
        if len(var_name) > 1 and var_name[-1] == 's':
            vars_data[var_name[:-1]] = vars_data[var_name]
            vars_data[var_name] = None



paris = '45456654'
s = 185
cosmos = {1, 2, 3}
print(paris)
print(cosmos)
change_var(paris)
print(paris)
print(cosmos)
print(vars())

