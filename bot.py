import os
import telebot
from flask import Flask, request

bot = telebot.TeleBot(os.environ["BOT_KEY"])
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome ' + message.entities[0].user.first_name + '! Start by sending me pictures of your food.")
