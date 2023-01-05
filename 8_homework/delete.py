def dell_data(out, id):
    out.pop(id)
    with open('Data.txt', 'w', encoding='utf-8') as file:
        for i in out:
            s = ''
            for j in i:
                s += f'{j} '
            s = s[:-1]
            file.write(f'{s}\n')
