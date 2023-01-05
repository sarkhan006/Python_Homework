def get_string(data):
    return data.split()

def look(date, id, search):
    cort = []
    for i in range(len(date)):  
        if search in date[i][id]:
            cort.append(date[i])
    return cort

