# 3 Вывести на экран числа от -N до N.

num = int(input("Введите целое число "))    # Считываем данные из консоли и с помощью int присваеваем ему численное значение


def print_num(number):              # создаем функцию 
    number = abs(number)            # задаем abs чтобы мы могли работать с отрицательными числами
    first = number*-1               # умножаем число на -1 чтобы добавить в нему минус
    second = number                 # в другую переменную кладем полученное число без изменений
    while first <= second:          # пока первое число меньше второго
        print(f'{first},', end='')  # печатаем первое число
        first += 1                  # счетчит


print_num(num)                      # вызываем функцию
