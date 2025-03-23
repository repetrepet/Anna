# Цикл While (цикл с условием)

counter = 1

# Цикл while выполняется, пока условие истинно
while counter <= 5:
    print(f'Counter is: {counter}')
    counter += 1  # Увеличиваем значение счетчика

# Бесконечный цикл (прервать можно вручную)
# while True:
#     number = input("Введите число: ")
#     print(f'Вы ввели число {number}')

# Использование break для выхода из цикла
while True:
    answer = input('Введите число (или "quit" для выхода): ')
    if answer == 'quit':
        break  # Завершаем цикл
    else:
        print(f'Вы ввели число {answer}')

# Задача 1: Сумма чисел
summa = 0
number = int(input('Введите число (0 для выхода): '))

while number != 0:
    summa += number  # Добавляем введенное число к сумме
    number = int(input('Введите число (0 для выхода): '))

print(f'Сумма чисел: {summa}')

# Задача 2: Угадай число
import random

random_number = random.randint(1, 100)
guess = int(input('Угадай число: '))

while guess != random_number:
    if guess < random_number:
        print('Больше!')
    elif guess > random_number:
        print('Меньше!')
    guess = int(input('Угадай число: '))

print("Поздравляю! Вы угадали число:", random_number)
