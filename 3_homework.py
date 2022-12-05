""" Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
 Пример:
 - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12"""

# list_input = []
# dimension = int(input('Введите размерность списка: '))
# summ = 0

# for i in range(dimension):
#     list_input.append(int(input(f'{i} позиция = ')))
#     if (i % 2 == 1):
#         summ += list_input[i]
# print(f'{list_input} сумма элементов стоящих на нечётных позициях = {summ}')



"""Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""

# list_input = []
# dimension_input = int(input('Введите размерность списка: '))
# list_output = []
# dimension_output = dimension_input / 2
# if(dimension_input % 2 == 1):
#     dimension_output += 1

# for i in range(dimension_input):
#     list_input.append(int(input(f'{i} позиция = ')))
# for i in range(int(dimension_output)):
#     list_output.append(int(list_input[i] * list_input[dimension_input - i - 1]))
# print(f'{list_input} => {list_output}')



"""Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19"""

# list_input = []
# list_output = []
# dimension = int(input('Введите размерность списка: '))

# for i in range(dimension):
#     list_input.append(float(input(f'{i} позиция = '))) 

# for i in list_input:
#     if (i // 1 != i):
#         list_output.append(round(float(i - (i // 1)).real, 10)) 

# max, min = list_output[0], list_output[0]
# for i in list_output:
#     if(min > i):
#         min = i
#     if(max < i):
#         max = i
# print(f'{list_input} => {max - min}')



"""Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""
# number = int(input('Введите число: '))
# binary = []
# count = 0

# while number != 0:
#     binary.append(int(number % 2))
#     number = int((number - binary[count]) // 2)
#     count += 1
# for i in range(count // 2):
#     binary[i], binary[count - 1 - i] = binary[count - 1 - i], binary[i]
# print(binary)



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

dimension = int(input('Введите размерность списка: '))
fibonacci_left = [1]
fibonacci_right = [1,1]

for i in range(2, dimension):
    fibonacci_right.append(int(fibonacci_right[i - 2] + fibonacci_right[i - 1]))
for i in range(1, dimension):
    fibonacci_left.append(int(fibonacci_right[i]))
    if(fibonacci_left[i - 1] > 0):
        fibonacci_left[i] *= -1
for i in range(dimension // 2):
    fibonacci_left[i], fibonacci_left[dimension - 1 - i] = fibonacci_left[dimension - 1 - i], fibonacci_left[i]

# Для вывода:
fibonacci_left.append(0)
for i in fibonacci_right:
    fibonacci_left.append(i)
print(fibonacci_left)