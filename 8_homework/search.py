def search(out, id, string):
    for i in out:
        if string in i[id]:
            for j in i:
                s = '' 
                for j in i:   
                    s += f'{j} '
            print(s)

def library():
    lib = {
        'FIO': 0,
        'Number': 1,
        'Jobs': 2,
        'Money': 3
    }
    s = '('
    for i in lib:
        s += f'{i}, '
    s = s[:-2] + ')'
    out = input(f'Введите поле по которому будет осуществлен поиск {s}: ')
    return(lib[out])