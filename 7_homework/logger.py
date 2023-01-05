def add_user(date):
    with open('file.csv', 'a', encoding='utf-8') as file:
        file.write(f'\n{date[0]};{date[1]};{date[2]}')

def output():
    libery = ['Last name', 'Name', 'Number']    
    data = []
    with open('file.csv', 'r', encoding='utf-8') as file:
        for i in file:
            data_libery = {}
            line = i.split(';')
            for j in range(len(line)):
                data_libery[libery[j]] = line[j]
            data.append(data_libery)
    return(data)

def edit(date):
    with open('file.csv', 'w', encoding='utf-8') as file:
        for i in date:
            file.write(f'{i[0]};{i[1]};{i[2]}')