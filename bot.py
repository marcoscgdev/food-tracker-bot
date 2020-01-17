import os
from flask import Flask, request
#from model_manager import ModelManager
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
    bot.reply_to(message, "Simply send me a picture of your foods. Then use /weekly or /daily commands to view the kcal report.")

def listener(messages):
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            tb.send_message(chatid, response(chatbot, text))

@bot.message_handler(content_types=['photo'])
def photo(message):
    file_url = "https://api.telegram.org/file/bot" + TOKEN + "/" + bot.get_file(message.photo[-1].file_id).file_path
    file_path = download_image(file_url)
    info = predict(file_path)
    message_to_send = generate_message(info)
    bot.send_message(message.chat.id, message_to_send)
    
bot.polling(none_stop=True, timeout=123)
bot.set_update_listener(listener) #register listener

@server.route('/', methods=['POST'])
def getMessage():
   bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "!", 200

if __name__ == "__main__":
   server.run(host="localhost", port=int(os.environ.get('PORT', 80)))