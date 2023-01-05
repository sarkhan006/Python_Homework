from datetime import datetime as dt

def log(out):
    time = dt.now().strftime('%H:%M')
    with open('Log.txt', 'a', encoding='utf-8') as file:
        file.write('{}: {}\n'.format(time, out))