# 1. В проекте, где вы решаете домашние задания, создайте модуль 'homework4.py'
# и напишите весь код в нём.
# СДЕЛАНО

# 2. Организуйте программу:
# - Создайте переменную my_string и присвойте ей значение строки с
#   произвольным текстом (функция input()).
my_string = (input("Введите название струнного музыкального инструмента,"
                   "который Вам нравится. Ответ должен начинаться с фразы '"'Мне нравится'"'. "))

# - Вывести длину символов введённого текста
dlina_struny=len(my_string)
print('В Вашем ответе содержится',
      dlina_struny, 'символов.')

# 3. Работа с методами строк:
#    Используя методы строк, выполните следующие действия:
# - Выведите строку my_string в верхнем регистре.
print(my_string.upper())

# - Выведите строку my_string в нижнем регистре.
print(my_string.lower())

# - Измените строку my_string, удалив все пробелы.
print(my_string.replace(' ', ''))

# Двойное подчёркивание получается и аргументы появляются, если задать команду так:
#print(my_string.replace('', ''))

# - Выведите первый символ строки my_string.
print(my_string[0])

# Выведите последний символ строки my_string.
print(my_string[-1])



