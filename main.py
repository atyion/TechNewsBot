from parser import *
import time
from config import api
import telebot


bot = telebot.TeleBot(api)
times=0
oldnews = ""


#Start command
@bot.message_handler(commands=['start'])
def start_command(message):
    global oldnews
    bot.send_message(message.chat.id, "Hi! Since now I'll send you the laster news about tech!")
    while True:
        time.sleep(5)
        if(parser()[3]!=oldnews):
            bot.send_message(message.chat.id, "<b>"+parser()[0]+"</b>"+"\n"+"<em>"+parser()[1]+"</em>"+"\n\n"+"<a href='"+parser()[2]+"'>Read more about it</a>", parse_mode= 'HTML')
            oldnews = parser()[3]




bot.infinity_polling()