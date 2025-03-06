# Булевый тип данных (True/False)

# Объявляем булевые переменные
is_student = True
is_rainy = False

# Выводим значения булевых переменных
print(is_student, is_rainy)

# Сравнение двух чисел
x = 10
y = 10
print(x == y)  # проверка на равенство

# Пример сравнения
x = 9
y = 10
is_equal = x == y  # сравнение (равны ли?)
print(is_equal)

# Другие операции сравнения
print(x != y)  # не равно
print(x < y)   # меньше
print(x > y)   # больше
print(x <= y)  # меньше или равно
print(x >= y)  # больше или равно

# Логические операции
x = 1
print(x < 5 and x > 0)  # и

x = 6
print(x < 5 and x > 0)  # и

x = 6
print(x < 5 or x > 0)   # или

# Логическое отрицание
is_student = False
print(not is_student)

is_student = True
print(not is_student)
