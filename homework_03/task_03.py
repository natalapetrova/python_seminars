# 3.Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers_list = [1.1, 1.2, 3.1, 5, 10.01, 0,5]
min_from_list = 1
max_from_list = 0
for i in numbers_list:
    if (i - int(i)) <= min_from_list:
        min_from_list = i - int(i)
    if (i - int(i)) >= max_from_list:
        max_from_list = i - int(i)  
print((max_from_list-min_from_list))