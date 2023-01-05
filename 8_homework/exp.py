def add_data(out):
    with open('Data.txt', 'a', encoding='utf-8') as file:
        file.write(f'{out}\n')

def add_string():
    fio = input('Введите ФИО: ')
    number = input('Введите телефон: ')
    jobs = input('Введите должность: ')
    money = input('Введите ЗП: ')
    return f'{fio} {number} {jobs} {money}'
    