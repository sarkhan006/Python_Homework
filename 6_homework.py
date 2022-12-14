# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Добавьте возможность использования скобок, меняющих приоритет операций.
# (1+2)*3 => 9
"""
number_list = []
char_list = []

def math(op, x, y):
    return (op(x, y))

def calc(char, col, st, en):
    global number_list
    global char_list
    if char == '*':
        number_list[col - st + en - 1] = math(lambda x, y: x*y, float(number_list[col - st + en - 1]), float(number_list[col - st + en]))
    elif char == '/': 
        number_list[col - st + en - 1] = math(lambda x, y: x/y, float(number_list[col - st + en - 1]), float(number_list[col - st + en])) 
    elif char == '+':
        number_list[col - st + en - 1] = math(lambda x, y: x+y, float(number_list[col - st + en - 1]), float(number_list[col - st + en])) 
    elif char == '-':
        number_list[col - st + en - 1] = math(lambda x, y: x-y, float(number_list[col - st + en - 1]), float(number_list[col - st + en])) 
    number_list.pop(col - st + en)
    char_list.pop(st)           


f = '26.3-((1+2.3*2)*9)/3'
operation = ['(', ')', '*', '/', '+', '-']
count = ''
flag = True
for i in f:
    for j in operation:
        if i == j:
            char_list.append(j)
            flag = False
            break
    if flag:
        count += i
    else:
        if count != '':
            number_list.append(count)
            count = ''
        flag = True
if count != '':
    number_list.append(count)

flag = False
while char_list:
    col = 0
    nach = 0
    end = 0    
    for i in range(len(char_list)):
        if char_list[i] == '*' or char_list[i] == '/' or char_list[i] == '+' or char_list[i] == '-':
            col += 1
        if char_list[i] == '(':
            nach = i + 1
            flag = True
        elif char_list[i] == ')':
            end = i - 1
            break
    if flag:              
        for j in range(end - nach + 1):
            flag_op = True
            for i in range(nach, end + 1):
                if char_list[i] == '*':
                    calc('*', col, i, end)
                    end -= 1
                    col -= 1
                    flag_op = False
                    break
                elif char_list[i] == '/':
                    calc('/', col, i, end)
                    end -= 1
                    col -= 1
                    flag_op = False
                    break
            if flag_op:
                for i in range(nach, end + 1):
                    if char_list[i] == '+':
                        calc('+', col, i, nach)
                        end -= 1
                        col -= 1
                    elif char_list[i] == '-':
                        calc('-', col, i, nach)
                        end -= 1    
                        col -= 1            
                break
        char_list.pop(end+1)
        char_list.pop(nach-1)
        flag = False
    else:
        for j in range(len(char_list)):         
            flag_op = True
            for i in range(len(char_list)):                
                if char_list[i] == '*':
                    calc('*', i + 1, i, i)
                    flag_op = False
                    break
                elif char_list[i] == '/':
                    calc('/', i + 1, i, i)
                    flag_op = False
                    break
            if flag_op:
                while char_list:
                    i = 0
                    if char_list[i] == '+':
                        calc('+', 1, 0, 0)
                    elif char_list[i] == '-':
                        calc('-', 1, 0, 0)             
                break

print(f'{f} => {round(number_list[0], 3)}')

"""

# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
"""
f = list(map(int, '1 2 3 5 1 5 3 10 22 35 48 2 48'.split()))
res = [1, 2, 3, 5, 1, 5, 3, 10, 22, 35, 48, 2, 48]
output = []
while f:
    flag = True
    i = 1
    while i != len(f):
        if f[0] == f[i]:
            flag = False
            f.pop(i)
            i -= 1
        i += 1
    if flag:
        output.append(f[0])
    f.pop(0)
print(f'{res} => {output}')
"""

# (необязательное) Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:

# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:

# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Порядок вывода команд произвольный.

# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
"""
count = int(input('Sample Input: '))
input_list = []
cort_list = [(0, 2)]
for i in range(count):
    input_list.append(list(input().split(';')))

output_set = []
for i in range(count):
    for j in cort_list[0]:
        output_set.append(f"{input_list[i][j]}")
output_set = set(output_set)
output_name = []
for i in output_set:
    output_name.append(i)

output_game = []
for k in output_name:
    col = 0
    for i in range(count):
        for j in cort_list[0]:
            if k == input_list[i][j]:
                col += 1
    output_game.append(col)

output_win = [[0,0,0,0] for i in range(len(output_game))]
for i in range(count):
    if int(input_list[i][1]) < int(input_list[i][3]):
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][2]:
                output_win[j][3] += 3
                output_win[j][0] += 1
                break
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][0]:
                output_win[j][2] += 1
                break
    elif int(input_list[i][1]) == int(input_list[i][3]):
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][0]:
                output_win[j][3] += 1
                output_win[j][1] += 1
                break
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][2]:
                output_win[j][3] += 1
                output_win[j][1] += 1
                break
    if int(input_list[i][1]) > int(input_list[i][3]):
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][0]:
                output_win[j][3] += 3
                output_win[j][0] += 1
                break
        for j in range(len(output_name)):
            if output_name[j] == input_list[i][2]:
                output_win[j][2] += 1
                break

output = []
for i in range(count):
    line = []
    line.append(output_name[i])
    line.append(output_game[i])
    for j in output_win[i]:
        line.append(j)
    output.append(line)
for i in range(count):
    output_string = output[i][0] + ': '
    for j in range(1, len(output[i])):
        output_string += str(output[i][j]) + ' '
    print(output_string)

    """