# 5 Реализовать алгоритм перемешивания списка.

import random
def mix_list(list_original):                                # Вводим функцию перемешивания
    list = list_original[:]                                 # Создаем пустые списки куда будем вкладывать перемешанные списки
    list_length = len(list)                                 # Задаем длину списка равную длине первого списка
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list
list = [0, 1, 2, 3, 4, 5]
mixed_list = mix_list(list)
print("Изначальный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)