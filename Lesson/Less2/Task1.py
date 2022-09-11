# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов

number = int(input('Введите число N: '))

value = 1
for _ in range(number):
    print(value, end=' ')
    value *= -3
    
