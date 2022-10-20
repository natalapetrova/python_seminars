# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from math import ceil

numbers = [2, 3, 4, 5, 6]                           # Вводим спсиок из чисел
multiplication = 0                                  # Вводим переменную для подсчета произведения (ответа)
result_list = []                                    # Создаем пустой список для внесения результатов
end = len(numbers)                                  # Вводим переменную равную значению длины списка
half = ceil(end / 2)                                # Находим середину списка ( с помощью ceil округляем результат в большую сторону)

for i in range(half):                               # Проходим циклом только до середины списка
    multiplication = numbers[i] * numbers[end-1]    # в переменной считаем произведение первого и последнего элемента
    result_list.append(multiplication)              # в пустой список добавляем результат умножения
    end = end - 1                                   # итерация , чтобы идти с конца к середине 
print(f'Произведение пар чисел списка {result_list}')       # Выводим результат в консоль
