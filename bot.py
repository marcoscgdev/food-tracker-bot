import os
import time
import re
from flask import Flask, request
from ObjectDetection.predict import predict
from utils.download_image import download_image
from utils.generate_message import generate_message
from chatbot.main import train, response
import telebot

TOKEN = "YOUR_TOKEN"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
chatbot = train()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome " + message.from_user.first_name + "! Start by sending me pictures of your food.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Simply send me a picture of your foods. Then I will tell you if is ok or not for you to eat that food.")

@bot.message_handler(commands=['about'])
def send_about(message):
    bot.reply_to(message, "Simple telegram bot created as a final project for the subject \"Inteligent Systems\".")

@bot.message_handler(content_types=['text'])
def reply(message):
    bot.reply_to(message, response(chatbot, message.text))

@bot.message_handler(content_types=['photo'])
def photo(message):
    file_url = "https://api.telegram.org/file/bot" + TOKEN + "/" + bot.get_file(message.photo[-1].file_id).file_path
    file_path = download_image(file_url)
    info = predict(file_path)
    message_to_send = generate_message(info)
    bot.reply_to(message, message_to_send)

@server.route('/', methods=['POST'])
def getMessage():
   bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "!", 200

def telegram_polling():
    try:
        bot.polling(none_stop=True, timeout=60) #constantly get messages from Telegram
    except:
        bot.stop_polling()
        time.sleep(10)
        telegram_polling()

if __name__ == "__main__":
   server.run(host="localhost", port=int(os.environ.get('PORT', 8000)))
   telegram_polling()