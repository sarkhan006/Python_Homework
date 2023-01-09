def search(out, id, string):
    s = ''
    for i in out:
        if string in i[id]:
            for j in i.values():   
                s += f'{j} '
            s += '\n'
    s = s[:-1]
    return(s)       