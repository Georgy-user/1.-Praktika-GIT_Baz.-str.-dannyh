# 1. В переменную example запишите любую строку.
example = 'pioneer'
# 2. Выведите на экран(в консоль) первый символ этой строки.
print(example[0])
# 3. Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
print(example[-1])
# 4. Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
print(example[3:])
# 5. Выведите на экран(в консоль) это слово наоборот.
# 5а. Вариант 1.
print(example[-1:-8:-1])
# 5б. Вариант 2.
print(example[::-1])
# 6. Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')
print(example[1::2])

