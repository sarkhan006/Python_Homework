""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 """

"""
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")
"""


""" Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

"""
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")
"""




"""
# Реализуйте алгоритм перемешивания списка.

import random
list_input = list(range(-10, 10, 3))
print(f'    Исходный список: {list_input}')
random.shuffle(list_input)
print(f'Перемешанный список: {list_input}')
"""

"""
Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

def func(n):
    return (1 + (1 / n)) ** n

number = int(input('Введите число: '))
list = {}
sum = 0
for i in range(1, number + 1):
    list[i] = func(i)
    sum += list[i]
print(round(sum.real, 3))

"""

"""

#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
number = int(input('Введите число: '))
list = []
for i in range(number):
    list.append(random.randint(-number, number))
print(f'Исходые значения списка: {list}')

file = open('file.txt', 'r') #6, 4, 2, 1, 0
output = 1
for i in file.read():
    if (i != '\n'):
        output *= list[int(i)]
print(f'Произведение чисел: {output}')
"""