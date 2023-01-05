from logger import *
from Import_user import *

def add():
    add_user(get_string(input('Введите данные(через пробел):')))

def out(date):
    for i in date:
        n = ''
        for j in i:
            if j != 'Number':
                n += f'{j}: {i[j]}, '
            else:
                n += f'{j}: '
        for j in i['Number']:
            if j != '\n':
                n += j
        print(n)

def search():
    s = input('Введите поле и ключевое слово для поиска(через пробел): ').split()
    print(out(look(output(),s[0],s[1])))