# 2.Задача 1 из домашней работы 3. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list_numbers = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd = sum(list_numbers[item] for item in range(1, len(list_numbers), 2))
odd_el = str([list_numbers[item] for item in range(1, len(list_numbers), 2)]).strip('[]')
print(f'Для списка {list_numbers} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')