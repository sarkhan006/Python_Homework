from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime as dt
from sympy import *
from spy import *
from exp import *
from write_data import *
from delete import *
from search import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_input(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_command(update: Update, context: CallbackContext):
    log_input(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/calc_help\n/sum_help\n/dict_help')

async def time_command(update: Update, context: CallbackContext):  
    log_input(update, context)    
    time = dt.now().strftime('%H:%M')
    await update.message.reply_text(f'{time}')

async def sum_command(update: Update, context: CallbackContext):
    log_input(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def calc_command(update: Update, context: CallbackContext):
    log_input(update, context)
    msg = update.message.text
    items = msg.split()
    if items[1] == 'r':
        output = Rational(1/1)
        if items[4] == '+':
            output = Rational(items[2]) + Rational(items[3])
        elif items[4] == '-':
            output = Rational(items[2]) - Rational(items[3])
        elif items[4] == '/':
            output = Rational(items[2]) / Rational(items[3])
        elif items[4] == '*':
            output = Rational(items[2]) * Rational(items[3])
        await update.message.reply_text(f'{Rational(items[2])} {items[4]} {Rational(items[3])} = {output}')
    elif items[1] == 'c':
        output = 0
        if items[4] == '+':
            output = complex(items[2]) + complex(items[3])
        elif items[4] == '-':
            output = complex(items[2]) - complex(items[3])
        elif items[4] == '/':
            output = complex(items[2]) / complex(items[3])
        elif items[4] == '*':
            output = complex(items[2]) * complex(items[3])
        await update.message.reply_text(f'{items[2]} {items[4]} {items[3]} = {output}')

async def sum_help(update: Update, context: CallbackContext):
    log_input(update, context)
    await update.message.reply_text(f'/sum 3 4')

async def calc_help(update: Update, context: CallbackContext):
    log_input(update, context)
    await update.message.reply_text(f'Rational: /calc r 5/3 9/2 * \
                                    \nComplex: /calc c 10+5j 5+3j *')

async def dict_help(update: Update, context: CallbackContext):
    log_input(update, context)
    await update.message.reply_text(f'Добавление: /dict a \"ФИО\" \"Телефон\" \"Работа\" \"Зарплата\"\
                                    \nВывод:      /dict w\
                                    \nПоиск:      /dict s \"(FIO/Number/Jobs/Money)\" \"Искомое слово\"\
                                    \nУдаление:   /dict d \"Номер записи\"')

async def dict_command(update: Update, context: CallbackContext):   
    msg = update.message.text
    items = msg.split()
    if items[1] == 'a':
        log_input(update, context)
        s = f'{items[2]},{items[3]},{items[4]},{items[5]}'
        add_data(s)
        await update.message.reply_text(f'Запись добавлена!')
    elif items[1] == 'w':
        log_input(update, context)
        await update.message.reply_text(f'{write_data(import_data())}')  
    elif items[1] == 'd':
        log_input_dell(update, context, file_list()[int(items[2])])
        dell_data(file_list(), int(items[2]))
        await update.message.reply_text(f'Запись удалена!')
    elif items[1] == 's':
        log_input(update, context)
        await update.message.reply_text(f'{search(file_list(), items[2], items[3])}')