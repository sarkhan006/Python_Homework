def import_data():
    imp = []
    with open('Data.txt', 'r', encoding='utf-8') as file:
        for i in file:
            s = ''
            for j in i:
                if j != '\n':
                    s += j
            imp.append(s.split(','))
    return imp

def write_data(out):
    ind_s = 0    
    my_dict = {
        0:'ФИО',
        1:'Телефон',
        2:'Работа',
        3:'Зарплата'
    }
    s = ''
    for i in out:
        key_d = 0
        s += f'{ind_s}: ' 
        for j in i:   
            s += f'{my_dict[key_d]} - {j}'
            key_d += 1
            if key_d != 4:
                s +='; '
        s += '\n'
        ind_s += 1
    return s