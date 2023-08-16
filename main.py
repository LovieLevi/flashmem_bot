import os
import sqlite3
# .env Support
from dotenv import load_dotenv
# Telegram Bot API
import telebot

# Consts
load_dotenv()
TOKEN = os.getenv("TOKEN")
DB_File = os.getenv("DB")

def DB_Check_table(name):
    conn = sqlite3.connect(DB_File)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT
    )
    ''')
    conn.commit()
    conn.close()
def DB_Get_all_users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    table_names_list = [name[0] for name in table_names]
    conn.close()
    print(table_names_list)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def start(message):
    DB_Check_table(message.chat.username)
    DB_Get_all_users()
    bot.reply_to(message, f'Hi {message.chat.first_name}, use menu to see commands.')

@bot.message_handler(commands=['add'])
def add(message):
    DB_Check_table(message.chat.username)
    args = message.text.split(" ")[1:]
    #if len(args).
    bot.reply_to(message, f'Args: {args}')

@bot.message_handler(commands=['buttons'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()

    button1 = telebot.types.InlineKeyboardButton(text='1️⃣', callback_data='0')
    button2 = telebot.types.InlineKeyboardButton(text='2️⃣', callback_data='1')
    button3 = telebot.types.InlineKeyboardButton(text='3️⃣', callback_data='0')
    button4 = telebot.types.InlineKeyboardButton(text='5️⃣', callback_data='0')

    markup.add(button1, button2, button3, button4)

    bot.send_message(message.chat.id, "มานีคีใจ\n1. Мани ведёт То искать краба.\n2. Мани рада.\n3. То рад.\n4. Мани привела То на поле.", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == '0':
        bot.send_message(call.message.chat.id, "Nope :(")
    elif call.data == '1':
        bot.send_message(call.message.chat.id, "Yup!")

bot.infinity_polling()
