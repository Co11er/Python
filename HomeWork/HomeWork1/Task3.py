# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите X : '))
y = int(input('Введите Y : '))

if x == 0 and y == 0:
    print('Четверти нет')
elif x > 0 and y > 0:
    print(f'Точка x = {x} y = {y} находиться в первой четверти')
elif x < 0 and y > 0:
    print(f'Точка x = {x} y = {y} находиться во второй четверти')
elif x < 0 and y < 0:
    print(f'Точка x = {x} y = {y} находиться в третьей четверти')
else:
    print(f'Точка x = {x} y = {y} находиться в четвертой четверти')
