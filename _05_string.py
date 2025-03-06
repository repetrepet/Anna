# --- Строки (String) ---

# Создание строки
my_string = 'Hello, world!'
print(my_string)

# Конкатенация строк (сложение строк)
first_name = 'Ann'
last_name = 'Smith'
full_name = first_name + ' ' + last_name
print(full_name)

# Функция len() - длина строки
print(len(full_name))
print(len(''))  # пустая строка

# Преобразование числа в строку
my_int = 123
my_string = str(my_int)
print(len(my_string))

# Длина большой строки (пример с числом 2^1000)
big_integer = 2 ** 1000
print(len(str(big_integer)))

# Проверка наличия подстроки в строке
my_string = "Hello, world!"
print('Hello' in my_string)  # True
print('x' in my_string)  # False

# --- Строковые методы ---

# Подсчет количества вхождений символа
string = 'Hello, world!'
print(string.count('l'))

# Форматирование строк (f-строка)
name = 'Bob'
age = 20
print(f'Привет, меня зовут {name}, мне {age} лет.')
