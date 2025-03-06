# --- Списки (List) ---

# Создание списка
fruits = ['apple', 'banana', 'cherry']
print(fruits)

# Преобразование строки в список
print(list("Hello!"))

# Длина списка
print(len(fruits))

# Список с разными типами данных
lst = [1, 'apple', True, 1.6, [1, 2, 3]]
print(lst)

# Сравнение списков
list1 = [1, 2, 3]
list2 = [1, 3, 2]
list3 = [1, 2, 3]
print(list1 == list2)  # False
print(list1 == list3)  # True

# Проверка наличия элемента в списке
print('apple' in fruits)  # True
print('watermelon' in fruits)  # False

# Сложение списков
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list2 + list1)

# --- Методы списков ---

# Добавление элемента в список
fruits.append('watermelon')
print(fruits)

# Удаление элементов списка
fruits.pop()  # Удаление последнего элемента
fruits.pop(0)  # Удаление элемента по индексу
print(fruits)

# Сортировка списка
l = ['a', 'y', 'd', 'h']
l.sort()
print(l)

# Разворот списка
fruits = [1, 2, 3, 4, 5]
fruits.reverse()
print(fruits)
