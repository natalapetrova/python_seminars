# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.

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


def get_coeff(polinom_string):
    polinom_dict = {}
    polinom_list = polinom_string.split(' ')
    sign = 1

    for pol_num in range(0, len(polinom_list) - 2):
        if polinom_list[pol_num][0] == '-' or polinom_list[pol_num] == '-':
            sign = -1
        if polinom_list[pol_num] not in ('+', '-'):
            if polinom_list[pol_num].find('x') == -1:
                polinom_dict[0] = int(polinom_list[pol_num]) * sign
                sign = 1
            elif polinom_list[pol_num].find('^') == -1 and polinom_list[pol_num].find('x') != -1:
                temp = polinom_list[pol_num].replace('x', '')
                if len(temp) == 0:
                    temp = 1
                polinom_dict[1] = int(temp) * sign
                sign = 1
            else:
                temp = polinom_list[pol_num].replace('^', '')
                if temp.find('-') != -1:
                    temp = temp.replace('-', '')
                temp = temp.split('x')
                if len(temp[0]) == 0:
                    temp[0] = 1
                polinom_dict[int(temp[1])] = int(temp[0]) * sign
                sign = 1
    return polinom_dict


def summ_dict(polinom_dict_1, polinom_dict_2):
    summ_dict = polinom_dict_1.copy()
    summ_dict.update(polinom_dict_2)

    for summ_keys in summ_dict:
        summ_dict[summ_keys] = polinom_dict_1.get(
            summ_keys, 0) + polinom_dict_2.get(summ_keys, 0)
    return summ_dict


def get_polynom_from_file(file_name):
    with open(file_name, 'r') as data:
        polygon_string = data.read()
        return polygon_string


file_1 = 'file_1.txt'
file_2 = 'file_2.txt'
file_3 = 'file_3.txt'

k = abs(int(input('Введите натуральную степень k первого многочлена: ')))
polynom_dict = get_polinom_dict(k)
write_polynom_to_file(polynom_dict, file_1)

k = abs(int(input('Введите натуральную степень k второго многочлена: ')))
polynom_dict = get_polinom_dict(k)
write_polynom_to_file(polynom_dict, file_2)

polynom_string_1 = get_polynom_from_file(file_1)
polynom_dict_1 = get_coeff(polynom_string_1)
print(polynom_dict_1)

polynom_string_2 = get_polynom_from_file(file_2)
polynom_dict_2 = get_coeff(polynom_string_2)
print(polynom_dict_2)

summ_polynom = summ_dict(polynom_dict_1, polynom_dict_2)
print(f'{"=" * 50}')
write_polynom_to_file(summ_polynom, file_3)