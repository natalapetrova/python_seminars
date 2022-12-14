# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# *Пример:*
# - Для n = 6:
#     [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
#     Сумма чисел = 14.0717

n = int(input('Введите число N: '))                             # Запрашиваем у пользователя число

def sequence(n):                                                # Вводим функцию которая принимает число введенное пользователем

    return[round((1 + 1 / x)**x, 4) for x in range (1, n + 1)]  # Создаем список, каждый элемент которого находится по формуле
        
print(sequence(n))                                              # Печатаем список
print(sum(sequence(n)))                                         # Суммируем список с помощью функции sum