# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = input('Введите первое значение: ')
y = input('Введите второе значение: ')
z = input('Введите третье значение: ')

if not(x or y or z) == (not(x) and not(y) and not(z)):
    print('Утверждение верно')
else:
    print('Утверждение ложно')

# Второй вариант решения

def logical(x,y,z):
    left = not (x or y or z)
    right = not x and not y and not z
    return left == right

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"x {x} y {y} z {z}")
            print(logical(z,y,z))