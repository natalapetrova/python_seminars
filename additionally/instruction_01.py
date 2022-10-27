# Ключевые аргументы
# Если имеется некоторая функция с большим числом параметров, и при ее вызове требуется указать только некоторые из них,
# значения этих параметров могут задаваться по их имени - это называется ключевые паарметры.


def func(a, b=5, c=10):
    print('a =', a, '  b =', b, '  c =', c)

func(3,7)
func(25, c=24)
func(c=50,a=100)



# Переменное число параметров (Variable number of Arguments)
# Иногда бывает нужно определить функцию, способную принимать любое число параметров. Этого можно достичь при помощи звёздочек *.
# Когда мы объявляем параметр со звёздочкой, все позиционные аргументы начиная с этой позиции и до конца будут собраны в кортеж.
# ** = все ключевые аргументы начиная с этой позиции и до конца будут собраны в словарь.

def total(a=5, *numbers, **phonebook):
    print('a', a)

    for single_item in numbers:
        print('single_item', single_item)

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))


# Строки документации
# Python имеет остроумную особенность, называемую строками документации, обычно обозначаемую сокращенно docstring.
# Этот инструмент помогает лучше документировать программу и облегчает ее понимание.
# Строку документации можно получить даже во время выполнения программы!

def print_max(x, y):
    ''' Выводит максимальное из двух чисел
    
    Оба значения должны быть целыми числами'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'bigest')
    else:
        print(y, 'bigest')

print_max(3,5)
print(print_max.__doc__)