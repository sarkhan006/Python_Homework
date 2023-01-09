from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *

app = ApplicationBuilder().token("5654866618:AAEYsL0hXqH9M4CH_4szIndUwQpGOjPywfY").build()

print('Server start')

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("dict", dict_command))
app.add_handler(CommandHandler("dict_help", dict_help))
app.add_handler(CommandHandler("sum_help", sum_help))
app.add_handler(CommandHandler("calc_help", calc_help))


app.run_polling()