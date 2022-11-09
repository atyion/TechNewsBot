import time
from main import users
from parser import *
import telebot
from config import api2
bot = telebot.TeleBot(api2)

@bot.message_handler(commands=['start'])
def start_command(message):
    while True:
        time.sleep(500)
        print("Update sent!\n")
        bot.send_message(message.chat.id, "/update")


    