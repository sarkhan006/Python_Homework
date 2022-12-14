# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""
string = input('Введите строку: ')
stringList = string.split()
string = ''
k = 0
while (k < len(stringList)):
    i = stringList[k]
    for j in range(len(i)):
        if (i[j] == 'а') & (j < (len(i) - 2)):
            if (i[j+1] == 'б') & (i[j+2] == 'в'):
                stringList.remove(i)
                k -= 1
    k += 1
for i in stringList:
    string += i + ' '
print(string)
"""



# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
"""
from tkinter import *
from tkinter import messagebox 
import random
from tkinter import scrolledtext

games = Tk()
games.title('Сandies')
game_run = True
candies_count = 2021
limits = 28
complexity = IntVar()
names = ['Player1: ', 'Player2: ', 'Computer: ']
move = 0
games.geometry('400x350')
text_progres = Label(games, text = 'Осталось конфет: 2021', font=('Verdana', 10))
pole = scrolledtext.ScrolledText(games, width=47, height=13, font=('Verdana', 10), state='disabled') 

def new_game():   
    global game_run
    game_run = True
    global candies_count
    candies_count = 2021
    global move
    move = 0
    text_progres.configure(text=f'Осталось конфет: 2021')
    pole.configure(state='normal')
    pole.delete(1.0, END)
    pole.configure(state='disabled')

def click(): 
    global candies_count 
    global complexity
    global move
    if (game_run) & (int(txt.get()) <= limits) & (int(txt.get()) <= candies_count): 
        write_complexity(int(txt.get()), names[move])     
        check_win(names[move], candies_count)
        if (game_run) & (candies_count != 0):
            if int(complexity.get()) == 0:
                if move == 0:
                    move = 1
                else:
                    move = 0 
            else:
                computer_move()

def write_complexity(count, name):
    global candies_count
    candies_count -= count
    res = "Осталось конфет: {}".format(candies_count)
    text_progres.configure(text=res) 
    pole.configure(state='normal')
    pole.insert(INSERT, f'{name}{count}\n')  
    pole.configure(state='disabled')             

def check_win(name, count):
    if count == 0:
        global game_run
        game_run = False
        messagebox.showinfo('Info', f'{name} Win!')

def computer_move():
    global complexity
    global candies_count
    count = 0
    write = 0
    if 1471 < candies_count < 1500:
        messagebox.showinfo('Computer', 'Тебе меня не победить!')
    if 300 < candies_count < 329:
        messagebox.showinfo('Computer', 'Сдавайся!')
    if (random.randint(1, 10) <= int(complexity.get())):
        while candies_count > count:
            count += 29           
        if candies_count == count:
            write = random.randint(1,28)
        elif candies_count > 29:
            write = candies_count - (count - 29)
        elif candies_count < 29:
            write = candies_count
    elif candies_count > 28:
        write = random.randint(1,28)
    elif candies_count < 29:
        write = candies_count   
    write_complexity(write, names[2])
    check_win(names[2], candies_count)

menu = Menu(games)  
new_games = Menu(menu)  
new_games.add_radiobutton(label= 'User', value=0, variable=complexity, command=new_game)
new_games.add_radiobutton(label= 'Easy', value=3, variable=complexity, command=new_game)
new_games.add_radiobutton(label= 'Medium', value=5, variable=complexity, command=new_game)
new_games.add_radiobutton(label= 'Hard', value=9, variable=complexity, command=new_game) 
menu.add_cascade(label = 'Games', menu = new_games)  
games.config(menu=menu) 
lbl = Label(games, text = 'Введите колличество конфет:', font=('Verdana', 10,))
txt = Entry(games, width=2, font=('Verdana', 15, 'bold'))
btn = Button(games, text='OK', width=3, 
             font=('Verdana', 15, 'bold'),
             background='lavender', command=click, )
new_button = Button(games, text='new game', command=new_game)
text_progres.grid(column=0, row=0)
pole.grid(column=0, row=1)
lbl.grid(column=0, row=2)
txt.grid(column=0, row=3)
btn.grid(column=0, row=4)
new_button.grid(row=5, column=0, columnspan=3, sticky='nsew')
games.mainloop()
"""


# Создайте программу для игры в ""Крестики-нолики"".
"""
from tkinter import *
import random
from tkinter import messagebox 

games = Tk()
games.title('Criss-cross')
game_run = True
pole = []
cross_count = 0

def new_game():
    for row in range(3):
        for col in range(3):
            pole[row][col]['text'] = ' '
            pole[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0

def click(row, col):
    if (game_run) & (pole[row][col]['text'] == ' '):
        pole[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if (game_run) & (cross_count < 5):
            computer_move()
            check_win('O')
        elif cross_count == 5:
            messagebox.showinfo('Info', 'Ничья!')

def check_win(smb):
    for n in range(3):
        check_line(pole[n][0], pole[n][1], pole[n][2], smb)
        check_line(pole[0][n], pole[1][n], pole[2][n], smb)
    check_line(pole[0][0], pole[1][1], pole[2][2], smb)
    check_line(pole[2][0], pole[1][1], pole[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:       
        global game_run
        game_run = False
        if a1['text'] == 'O':
            a1['background'] = a2['background'] = a3['background'] = 'red'
            messagebox.showinfo('Info', 'Lose!')
        else:
            a1['background'] = a2['background'] = a3['background'] = 'green'
            messagebox.showinfo('Info', 'Win!')

def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(pole[n][0], pole[n][1], pole[n][2], 'O'):
            return
        if can_win(pole[0][n], pole[1][n], pole[2][n], 'O'):
            return
    if can_win(pole[0][0], pole[1][1], pole[2][2], 'O'):
        return
    if can_win(pole[2][0], pole[1][1], pole[0][2], 'O'):
        return
    for n in range(3):
        if can_win(pole[n][0], pole[n][1], pole[n][2], 'X'):
            return
        if can_win(pole[0][n], pole[1][n], pole[2][n], 'X'):
            return
    if can_win(pole[0][0], pole[1][1], pole[2][2], 'X'):
        return
    if can_win(pole[2][0], pole[1][1], pole[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if pole[row][col]['text'] == ' ':
            pole[row][col]['text'] = 'O'
            break

for row in range(3):
    line = []
    for col in range(3):
        button = Button(games, text=' ', width=4, height=2, 
                        font=('Verdana', 25, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    pole.append(line)
new_button = Button(games, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
games.mainloop()

"""