import telebot

bot = telebot.TeleBot(os.environ["BOT_KEY"])

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome ' + message.entities[0].user.first_name + '! Start by sending me pictures of your food.")
