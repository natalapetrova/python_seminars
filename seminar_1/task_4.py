# 4 Показать первую цифру дробной части числа.

num = float(input("Введите число: "))               # В переменную вносим значения из терминала бозначаем тип данных float(дробное число)#5.25
round_num = int(num)                                # В другую переменную вносим полученное число как целочисленное(округаляем) #5
result = (num - round_num) * 10                     # 5.25 - 5 = 0.25 * 10 =2.5 с помощью int округляем до целого 2
print(f' первая цифра дроброй части {int(result)}') # Печатаем результат