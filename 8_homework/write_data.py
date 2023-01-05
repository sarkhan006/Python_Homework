def import_data():
    imp = []
    with open('Data.txt', 'r', encoding='utf-8') as file:
        for i in file:
            s = ''
            for j in i:
                if j != '\n':
                    s += j
            imp.append(s.split())
    return imp
    