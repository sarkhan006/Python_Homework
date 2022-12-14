""" Вычислить число c заданной точностью d """

# d = float(input('Введите точность: '))
# number = float(input('Введите число: '))
# count = 0

# while d < 1:
#     count += 1
#     d *= 10
# print(f'%.{count}f' % number)


"""Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N."""

# import sympy

#output = {0}
#count = 1

#output.clear()
#while number > 1:
#    if number / sympy.prime(count) != number // sympy.prime(count):
#        count += 1
#    else:
#        output.add(sympy.prime(count))
#        number /= sympy.prime(count)
#        count = 1       
#print(output)


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N."""

"""import sympy

number = int(input('Введите число: '))
output = {0}
count = 1

output.clear()
while number > 1:
    if number / sympy.prime(count) != number // sympy.prime(count):
        count += 1
    else:
        output.add(sympy.prime(count))
        number /= sympy.prime(count)
        count = 1       
print(output) """


# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

# проверка на первое входжение
"""def addstring(f, s):
    if f:
        return s
    else:
        return ' + ' + s

degree = {'0':'⁰', '1':'¹', '2':'²', '3':'³', '4':'⁴', '5':'⁵', '6':'⁶', '7':'⁷', '8':'⁸', '9':'⁹'}
k = int(input('Введите степень: '))
start = True
output = f'При k = {k}: '
number = 0

while k >= 0:
    number = random.randint(0, 100)
    if (number > 1) & (k != 0):
        output += addstring(start, f'{str(number)}x')
        start = False
        for a in str(k):
            output += degree.get(a)
    elif (number == 1) & (k != 0):
        output += addstring(start, 'x')
        start = False
        for a in str(k):
            output += degree.get(a)
    elif (number != 0) & (k == 0):
        output += addstring(start, f'{str(number)} = 0')
    elif (number == 0) & (k == 0):
        output += ' = 0'
    k -= 1
print(output)
"""


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# Подсчет повторяющихся элементов многочлена
"""def calc(string = '', numbers = 0):
    numberStr = ''
    const = 1
    if (string[0] == '+') & (string[1] != 'x'):
        while (string[const] != 'x'):
            numberStr += string[const]
            const += 1
            if (const == len(string)):
                break
        numbers += int(numberStr)
    elif (string[0] == '+') & (string[1] == 'x'):
        numbers += 1
    elif (string[0] == '-') & (string[1] != 'x'):
        while (string[const] != 'x'):
            numberStr += string[const]
            const += 1
            if (const == len(string)):
                break
        numbers -= int(numberStr)
    elif (string[0] == '-') & (string[1] == 'x'):
        numbers -= 1
    return numbers

# Перенос из файлов в строку
fileFirst = open('file1.txt', 'r')
fileSecond = open('file2.txt', 'r')
line = '+'
for l in fileFirst:
    line += l
line += ' '
for l in fileSecond:
    line += l
fileFirst.close()
fileSecond.close()

# Данные для сложения
listElements = line.split()
elements = ['xВі', 'xВІ', 'x', ' ']
output = ''
start = True

# Формирование ответа
for i in range(4):
    j = 0
    number = 0    
    while (j < len(listElements)):
        if i != 3:
            if set(elements[i]).issubset(listElements[j]):
                number = calc(listElements[j], number)   
                listElements.remove(listElements[j])
            else:
                j += 1        
        else:
            number = calc(listElements[j], number)    
            listElements.remove(listElements[j]) 
    if (number > 0):
        if (start):
            output += str(number) + elements[i]
            start = False
        else:
            output += ' +' + str(number) + elements[i]
    else: 
        if (start):
            output += str(number) + elements[i]
            start = False  
        else:
            output += ' ' + str(number) + elements[i]
print(output)

# Вывод в файл
o = open('file3.txt', 'w')
o.writelines(output)
o.close() """