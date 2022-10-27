#Программа которая на вход принимает 5 чисел и находит максимальное из них

# Первый вариант решения
my_list = []
for i in range(5):
    my_list.append(input('--->'))
print(my_list)

# Второй вариант решения
my_list_1 = [3, 5, 1, 2, 8]
print(max(my_list_1))

# Третий вариант решения
my_list_2 = [6, 9, 2, 4, 0]
maxx = my_list_2[0]
for item in my_list_2:
    if item > maxx:
        maxx = item
print(maxx)

# Четвертый вариант решения
my_list_3 = [61, 92, 32, 44, 50]
maxx_1 = my_list_2[0]
for i in range(len(my_list_3)):
    if my_list_3[i] > maxx:
        maxx = i
print(maxx_1)



# 3 Вывести на экран числа от -N до N.
n = int(input('Введите число N: '))
for i in range(-n, n + 1):
    print(i, end=' ')



# 4 Показать первую цифру дробной части числа.
number = input('Введите дробное число: ')
print(number.split('.')[1][0])

# Второй вариант решения
number_1 = float(input('Введите дробное число: '))
number_1 *= 10
number_1 = int(number_1)
print(number_1 % 10)


# Чтобы узнать значение функции или метода можно обратиться к "help"
help(range)



#  Зарезервированное слово "nonlocal"
def func_outer():
    x = 2
    print('x = ', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print(' x ', x)
    
func_outer()