# ==============================================================
# Программа для работы с числами: ввод, вычисления, вывод
# ==============================================================

# 1. Запрашиваем у пользователя 5 чисел, сохраняем в список
# 2. Вычисляем сумму чисел и их среднее значение
# 3. Выводим результаты на экран

# Создаем пустой список для хранения чисел
numbers = []

# Цикл для запроса 5 чисел у пользователя
for _ in range(5):
    number = int(input("Введите число: "))  # Запрос числа у пользователя
    numbers.append(number)  # Добавляем число в список

# Вычисляем сумму всех чисел в списке
sum_numbers = sum(numbers)

# Вычисляем среднее арифметическое (сумма / количество элементов)
average = sum_numbers / len(numbers)

# Выводим результаты
print(f"Сумма чисел: {sum_numbers}")
print(f"Среднее значение: {average}")

# ==============================================================
# Программа для вывода квадратов чисел в заданном диапазоне
# ==============================================================

# 1. Запрашиваем у пользователя два целых числа (начало и конец диапазона)
# 2. Проверяем корректность ввода (начальное число < конечного)
# 3. Вычисляем и выводим квадраты всех чисел в диапазоне

# Запрашиваем начальное и конечное число
start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))

# Проверяем корректность диапазона
if start >= end:
    print("Ошибка! Начальное число должно быть меньше конечного.")
else:
    # Перебираем числа в заданном диапазоне
    for number in range(start, end + 1):
        square = number ** 2  # Вычисляем квадрат числа
        print(f"Квадрат числа {number} равен {square}")

# ==============================================================
# Демонстрация форматированного вывода строки с переменной
# ==============================================================

# Задаем переменную с возрастом
age = 10

# Вывод с использованием f-строки
print(f"Привет, друг! Мне {age} лет")

# Вывод с использованием запятой (разделяет аргументы пробелом)
print("Привет, друг! Мне", age, "лет")
