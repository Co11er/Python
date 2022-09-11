# Для натурального N создатьь последовательность 3N + 1

number = int(input('Введите число N: '))
list = []
for i in range(1,number + 1):
    num = (3 * i) + 1
    print(f'{i}: {num}')

