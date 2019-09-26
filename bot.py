import requests  
import os
from flask import Flask, request

BOT_URL = f'https://api.telegram.org/bot{os.environ["BOT_KEY"]}/'  # <-- add your telegram token as environment variable


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():  
    data = request.json

    #print(data)  # Comment to hide what Telegram is sending you
    chat_id = data['message']['chat']['id']
    message = data['message']['text']
    first_name = data['message']['chat']['first_name']

    if message == '/start':
        sendMessage(chat_id, 'Welcome ' + first_name + '! Start by sending me pictures of your food.')
        
    if message == '/about':
        sendMessage(chat_id, 'A simple an easy to use food tracker bot. Made by Marcos Calvo and Marcos Caballero.')

    return ''

def sendMessage(chat_id, message):
    json_data = {
        "chat_id": chat_id,
        "text": message,
    }
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=json_data)

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
