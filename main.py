from parsernews import *
import threading
#import datetime
import time
from config import api
import telebot

print("Starting bot...\n")

bot = telebot.TeleBot(api)
with open('chatid.txt') as f: 
    users = f.readlines() 
oldnews = ""
print(users)

def message_timer():
    while True:
        #if datetime.datetime.now().minute%2 == 0 and datetime.datetime.now().minute != tempo:
        #tempo = datetime.datetime.now().minute
        #
        #
        # EVERY 500 SECONDS
        time.sleep(500)
        update_command()
     
#Start command   
@bot.message_handler(commands=['start'])
def start_command(message):
    global oldnews
    if str(message.chat.id)+"\n" not in users:
        bot.send_message(message.chat.id, "Hi! From now I'll send you the lastest news about tech! \nIf you don't want more news write me /stop!")
        with open('chatid.txt', 'a') as file:
            users.append(str(message.chat.id)+'\n')
            file.write(str(message.chat.id)+"\n")
        print(message.chat.id)



#Update command
#@bot.message_handler(commands=['update'])
def update_command():
    global oldnews
    with open("news.txt",'r+') as file:
        oldnews = file.readline()
        
    if(parser()[0]!=oldnews):
        print("Sending news...\n")
        lenn = len(users)
        for i in range(lenn):
            try:
                bot.send_message(users[i], "<b>"+parser()[0]+"</b>"+"\n"+"<em>"+parser()[1]+"</em>"+"\n\n"+"<a href='"+parser()[2]+"'>Read more about it</a>", parse_mode= 'HTML')
                print("sent ", i+1, "/",lenn)
                with open("news.txt",'r+') as file:
                    file.truncate(0)
                    file.write(parser()[0])
            except:
                print("user blocked...")
                stopblock(users[i])

def stopblock(userid):
    
    if str(userid)+"\n" in users:
            users.pop(users.index(str(userid)+"\n"))
            print(userid, "removed")
            with open("chatid.txt",'r+') as file:
                    file.truncate(0)
                    for i in range(len(users)):
                        file.write(users[i]+"\n")



#Stop Command
@bot.message_handler(commands=['stop'])
def stop_command(message):
    if str(message.chat.id)+"\n" in users:
        users.pop(users.index(str(message.chat.id)+"\n"))
        bot.send_message(message.chat.id, "We won't send you more news! \nIf you want to restart the bot, write /start")
        print(message.chat.id, "removed")
        with open("chatid.txt",'r+') as file:
                file.truncate(0)
                for i in range(len(users)):
                    file.write(users[i]+"\n")
    else:
        bot.send_message(message.chat.id, "Already stopped!")

def bott():
    bot.infinity_polling()
x = threading.Thread(target=message_timer)
y = threading.Thread(target=bott)
y.start()
x.start()

