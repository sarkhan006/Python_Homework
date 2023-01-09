from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime as dt

def log_input(update: Update, context: CallbackContext):
    time = dt.now().strftime('%H:%M')
    file = open('log.csv', 'a', encoding='utf-8')
    file.write(f'{time}, {update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close

def log_input_dell(update: Update, context: CallbackContext, out):
    time = dt.now().strftime('%H:%M')
    file = open('log.csv', 'a', encoding='utf-8')
    file.write(f'{time}, {update.effective_user.first_name}, {update.effective_user.id}, {update.message.text} ({out})\n')