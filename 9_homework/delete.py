import csv

def dell_data(out, id):
    out.pop(id)
    file = open("Data.txt", 'w', encoding='utf-8')
    for i in out:
        s = ''
        for j in i.items():      
            s += j[1]
            if j[0] != 'Money':
                s += ','
        file.write(s + '\n')
    file.close

    with open("Date.csv", mode="w", encoding='utf-8') as w_file:
        names = []
        for i in out[0].keys():
            names.append(i)
        file_writer = csv.DictWriter(w_file, delimiter = ",", 
                                    lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        for i in out:
            file_writer.writerow(i)

def file_list():
    my_dict = []
    with open("Date.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter = ",")
        for i in file_reader:
            my_dict.append(i)
        return my_dict