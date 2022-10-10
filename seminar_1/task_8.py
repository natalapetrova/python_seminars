# 8 Сообщить в какой четверти координатной плоскости или на какой
# оси находится точка с координатами Х и У.

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
