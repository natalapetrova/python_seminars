# 1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# - Для N = 5: 1, -3, 9, -27, 81

n = int(input("Введите натуральное число n "))
result = " "
sign = 1

for i in range(0, n):
    result += str(3**i*sign)
    result += ", "
    sign = -sign
print(result[0:(len(result) - 2)])
