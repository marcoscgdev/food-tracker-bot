import os
import telebot
from flask import Flask, request

bot = telebot.TeleBot(os.environ["BOT_KEY"])
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome ' + message.entities[0].user.first_name + '! Start by sending me pictures of your food.")

if __name__ == '__main__':  
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
