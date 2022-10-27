# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


def input_num_candy(candy_qu):
    num = (input('\nВведите количество конфет которые вы хотите взять '))
    if num.isdigit():
        num = int(num)
        if num > candy_qu:
            print(
                f'\nНельзя взять конфет больше 28 и больше чем осталось, всего осталось {candy_qu} конфет')
            return input_num_candy(candy_qu)
        elif num > 28:
            print('\nВы взяли больше 28 конфет, так нельзя, возьмите заново')
            return input_num_candy(candy_qu)
        elif num == 0:
            print('\nНу возьмите хоть одну конфетку')
            return input_num_candy(candy_qu)
        else:
            return num
    else:
        print('\nНужно ввести целое число')
        return input_num_candy(candy_qu)


def bot_motion(candy_qu):
    if candy_qu > 80:
        res = random.randint(1, 29)
        return res
    elif candy_qu <= 28:
        res = candy_qu
        return res
    else:
        atemp = candy_qu//28
        if atemp == 1:
            f = candy_qu
            temp = f
            while f >= 29:
                res = temp-29
                f -= 1
                if res == 0:
                    res += 1
            return res

        res = candy_qu-(atemp)*28+1

    return res


def main_game(bot=False):
    print('\nНачинаем игру с конфетами 2021 !\nДавайте представимся')

    name_player_1 = input('\nВведите имя первого игрока: ')
    if bot:
        name_player_2 = "Bot"
    else:
        name_player_2 = input('\nВведите имя второго игрока: ')
    print(
        f'\nИграет игрок номер 1 {name_player_1} против игрока {name_player_2}')
    print('\nЗа один ход можно забрать не более чем 28 конфет')
    one_player = ""
    two_player = ""
    print('\n\nтеперь определим кто ходит первым')
    i = random.randint(1, 2)
    if i == 1:
        one_player, two_player = name_player_1, name_player_2
    else:
        one_player, two_player = name_player_2, name_player_1

    print(f'\nПо результатам жеребьевки первым ходит игрок {one_player}')

    candy_quant = 120
    all_candy_first = 0
    all_candy_second = 0
    last_player_1 = 0

    print(f'\nВсего конфет {candy_quant}')
    while candy_quant > 0:
        print(f'\nХодит игрок {one_player}')
        if one_player == "Bot":
            first = int(bot_motion(candy_quant))
        else:
            first = int(input_num_candy(candy_quant))
        all_candy_first += first
        candy_quant -= first
        last_player_1 = 1
        print(f'\nосталось {candy_quant}')
        if candy_quant > 0:
            if two_player == "Bot":
                second = int(bot_motion(candy_quant))
            else:
                second = int(input(candy_quant))
            print(f'\nХодит игрок {two_player} и взял {second}')
            all_candy_second += second
            candy_quant -= second
            last_player_1 = 0
        print(f'\nосталось {candy_quant}')

    print(
        f'\nВ итоге конфет у {one_player} {all_candy_first} конфет у {two_player} {all_candy_second}')
    if last_player_1 == 1:
        print(
            f'\nТак как последним забрал конфеты игрок по имени {one_player}, то он выиграл и забрал все конфеты')
    else:
        print(
            f'\nТак как последним забрал конфеты игрок по имени {two_player}, то он выиграл и забрал все конфеты')


bot_or_humans = input(
    '\nБудем играть с ботом ? Введите да иначе играют 2 игрока: ')

if bot_or_humans.lower() == "да":
    main_game(True)
else:
    main_game()
