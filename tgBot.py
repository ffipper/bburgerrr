import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('401643678:TEST:e46389b1-8055-4202-9909-8cbd0df6d95b')
STORE_URL = os.getenv('https://ffipper.github.io/bburgerrr/')
bot = telebot.TeleBot(5780310869:AAGEV9Sg3yjtwogIDM_zGDDGyGC408ZMij4)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
itembtn1 = types.KeyboardButton(text='Заказать полезную еду!', web_app=types.WebAppInfo(url=STORE_URL))
markup.add(itembtn1)

# markup = types.InlineKeyboardMarkup()
# itembtn1 = types.InlineKeyboardButton('Text',web_app=types.WebAppInfo(url=''))
# markup.add(itembtn1)

# markupmenu = types.MenuButtonCommands()
# menubtn1= types.MenuButton()

@bot.message_handler(commands=['start'])
@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, 'Заказываем?', reply_markup=markup)
    print(message)


@bot.message_handler(commands=['chatid'])
def chatid(message):
    print(message)
    bot.reply_to(message, 'Your chat id is: ' + str(message.chat.id))


print('Telegram bot starting...')

bot.infinity_polling()
