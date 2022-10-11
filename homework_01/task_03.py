# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

number_x = int(input("Введите x "))
number_y = int(input("Введите y "))


def quater(x, y):
    text = None
    if x > 0 and y > 0:
        text = "Первая четверть"
    elif x > 0 and y < 0:
        text = "Вторая четверть"
    elif x < 0 and y < 0:
        text = "Третья четверть"
    elif x < 0 and y > 0:
        text = "Четвёртая четверть"
    elif x == 0 and y == 0:
        text = "Пересечение координатных осей"
    elif x == 0 and y != 0:
        text = "Ось X"
    elif x != 0 and y == 0:
        text = "Ось Y"
    return text


print(quater(number_x, number_y))