from work import *

def Button_click():
    print('1 - Добавление данных\n\
2 - Просмотр данных\n\
3 - Поиск\n')
    command = input()
    if command == '1':
        add()
    elif command == '2':
        out(output())
    elif command == '3':
        search()