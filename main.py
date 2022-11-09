from parser import *
import time
from config import api
import telebot
from parser import *
import time
from config import api
import telebot

print("Starting bot...\n")

bot = telebot.TeleBot(api)
with open('chatid.txt') as f: 
    users = f.readlines() 
oldnews = ""
print(users)


#Start command
@bot.message_handler(commands=['start'])
def start_command(message):
    global oldnews
    bot.send_message(message.chat.id, "Hi! Since now I'll send you the lastes news about tech! \nIf you don't want more news write me /stop!")
    if message.chat.id not in users:
        with open('chatid.txt', 'a') as file:
            file.write(str(message.chat.id))
        print(message.chat.id)


#Update command
@bot.message_handler(commands=(['update']))
def update_command(message):
    global oldnews
    if(parser()[3]!=oldnews):
        print("Sending news...\n")
        for i in range(len(users)):
            bot.send_message(users[i], "<b>"+parser()[0]+"</b>"+"\n"+"<em>"+parser()[1]+"</em>"+"\n\n"+"<a href='"+parser()[2]+"'>Read more about it</a>", parse_mode= 'HTML')
            oldnews = parser()[3]
bot.infinity_polling()
