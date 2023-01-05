from log import *
from exp import *
from write_data import *
from delete import *
from search import *


def Button_Click():
    print('Введите команду:\
        \n1 - Добавить человека\
        \n2 - Вывести список\
        \n3 - Осуществить поиск')
    command = input()
    if command == '1':
        s = add_string()
        add_data(s)
        log(f'Add - {s}')
    elif command == '2':
        data = import_data()
        ind = 0
        for i in data:
            s = f'{ind}: ' 
            for j in i:   
                s += f'{j} '
            print(s)
            ind += 1
        log('Print data')
        c = input('Желаете удалить запись (y/n)')
        if c == 'y':
            id = int(input('Введите номер записи которую хотите удалить: '))
            log(f'Delete - {data[id]}')
            dell_data(data, id)
    elif command == '3':
        id = library()
        string = input('Введите искомое слово: ')
        log(f'Search - {id}, {string}')
        search(import_data(), id, string)
    else:
        print('Error!')