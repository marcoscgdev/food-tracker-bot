import os
import telebot
from flask import Flask, request

bot = telebot.TeleBot(os.environ["BOT_KEY"])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome ' + message.entities[0].user.first_name + '! Start by sending me pictures of your food.")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Simply send me a picture of your foods. Then use /weekly or /daily commands to view the kcal report.")

bot.polling()
