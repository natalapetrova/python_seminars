# 4 Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Random - создание многочлена - словаря. Ключи - степени, значения - коэффициенты. На входе степень многочлена.


import random


def get_polinom_dict(k):
    polynom_dict = {}

    while k != -1:
        coeff = random.randint(0, 100)
        polynom_dict[k] = coeff
        k -= 1
    return polynom_dict


def write_polynom_to_file(polynom_dict, file_name):
    text_string = ''
    max_degree = max(polynom_dict.keys())

    for degree in range(max_degree, -1, -1):
        if polynom_dict[degree] != 0:
            if polynom_dict[degree] > 0:
                sign = '+'
            else:
                sign = '-'
            if abs(polynom_dict[degree]) == 1 and degree != 0:
                temp = ''
            else:
                temp = str(abs(polynom_dict[degree]))
            if degree == 0:
                text_string += sign + ' ' + temp
            elif degree == 1:
                text_string += sign + ' ' + temp + 'x '
            else:
                text_string += sign + ' ' + temp + f'x^{degree} '
    if text_string[-1] == ' ':
        text_string += '= 0'
    else:
        text_string += ' = 0'
    if text_string[0] == '+':
        text_string = text_string[2:]

    with open(file_name, 'w') as data:
        data.write(text_string)
    print(f'Random-многочлен: {text_string} записан в файл {file_name}')


k = abs(int(input('Введите натуральную степень k: ')))
polynom_dict = get_polinom_dict(k)
print(f'Словарь-полином: {polynom_dict}')
file_name = 'file.txt'
write_polynom_to_file(polynom_dict, file_name)