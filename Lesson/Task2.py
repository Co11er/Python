# 2. Напишите программу, которая
# на вход принимает 5 чисел и находит максимальное из них.

# num_1 = int(input('Введите число 1: '))
# num_2 = int(input('Введите число 2: '))
# num_3 = int(input('Введите число 3: '))
# num_4 = int(input('Введите число 4: '))
# num_5 = int(input('Введите число 5: '))
# max = num_1
# list = [num_1, num_2, num_3, num_4, num_5]
list = []
for i in range(5):
    list.append(input('---> '))
print(list)
maxx = list[0]              # заполнение списка


for i in list[1:]:
    if i > maxx:
        maxx = i
print(maxx)                 # нахождение максимал числа в списке



for i in range(1, len(list)):
    if list[i] > maxx:
        maxx = i                    # нахождения индекса максимального

# print(max(list)) # нахождение MAX
# print(min(list)) # нахождение MIN
# print(sum(list)) # нахождение Cуммы элементов списка