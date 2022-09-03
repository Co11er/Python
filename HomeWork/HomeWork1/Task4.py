# Напишите программу, которая по заданному
# номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти : '))

if  quarter < 1 or quarter > 4:
    print('Четверти нет')
elif quarter == 1:
    print(f'В четверти {quarter} координаты по X > 0 Y > 0')
elif quarter == 2:
    print(f'В четверти {quarter} координаты по X < 0 Y > 0')
elif quarter == 3:
    print(f'В четверти {quarter} координаты по X < 0 Y < 0')
else:
    print(f'В четверти {quarter} координаты по X > 0 Y < 0')