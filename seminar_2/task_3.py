# 3.Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой.

from unittest import result


first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")
result = first_string.count(second_string)
print(f"Количество вхождений второй строки в первую {result}")
