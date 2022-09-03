print('hello')

# типы переменных и данных 
# int, float, boolean, str, list, None

a = 123 #- int
b = 1.23 #- float
s = 'hello' #- str
f = True #- boolean

# type(переменная) - команда узнать тип переменной

print(a, b, s)
print('{} {}'.format(a, b,)) # вариант вывода
print(f'{a} {b}') # вариант вывода

list = [] # создание списка

print('Введите a')
a = int(input())
print('Введите b')
b = int(input())
print(a, '+', b, '=', a + b)

a = 123
b = 321
c = a + b

print(c)

# работа со строками 

text = 'жили были дед и баба'
print(len(text))                # 20 
print('жили' in text)           # True
print(text.isdigit())           # Являються ли числами (False)
print(text.islower())           # Являються ли сивломами нижнего регистра (True)
print(text.replace('жили', 'ЖИЛИ'))

# Чтобы проверить за что отвечает
# данная функция использовать команду
# help(Вводим данную функцию)

# обрезка
text = 'съешь ещё немного этих мягких французских булок'
print(text[0])              # c
print(text[1])              # ъ
print(text[len(text)-1])    # к
print(text[-5])             # б
print(text[:])              # print(text)
print(text[:2])             # съ
print(text[len(text)-2:])   # ок
print(text[2:9])            # ешь ещё
print(text[6: -18])         # ещё этих мягких
print(text[0: len(text) : 6])# сеикакл
print(text[: : 6])          # сеикакл
text = text[2 : 9] + text[-5] + text[:2] 

text.append('слово') # добавить в конец списка
text.remove('слово') # удалить элемент