# Напишите программу, в которой пользователь будеть задавать
# две строки, а в программе определять количество вхождений одной строки в другой


str1 = input('Введите строку: ')
str2 = input('Введите строку: ')

count = 0
for i in range(0, len(str1) - len(str2)):
    if str2 == str1[i: i + len(str2)]:
        count += 1
print(f'{count} раз')