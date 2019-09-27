import os
from flask import Flask, request
import telebot

bot = telebot.TeleBot(os.environ["BOT_KEY"])
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome user! Start by sending me pictures of your food.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Simply send me a picture of your foods. Then use /weekly or /daily commands to view the kcal report.")

bot.polling()

@server.route('/', methods=['POST'])
def getMessage():
   bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "!", 200

if __name__ == "__main__":
   server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
