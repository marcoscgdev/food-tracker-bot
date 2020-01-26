# Food Tracker BOT
A simple an easy to use food tracker Telegram bot.

---

## About

Telegram bot that, based on the photos you send to, tells if you should improve or not your diet based on how healthy or unhealthy is the food you eat on a weekly basis. Users can also have a conversation with the bot as if it were a human.

## Developing

### Requirements

- [Python 3.6.1](https://www.python.org/downloads/release/python-361/)

#### Libraries

- [Flask 1.1.1](https://www.palletsprojects.com/p/flask/)
- [pyTelegramBotAPI 3.6.6](https://github.com/eternnoir/pyTelegramBotAPI)
- [Pillow 7.0.0](https://pillow.readthedocs.io/en/stable/index.html)
- [chatterBot 1.0.5](https://chatterbot.readthedocs.io/en/stable/quickstart.html)
- [pandas 0.25.3](https://pandas.pydata.org/)
- [keras 2.2.4](https://keras.io/)
- [scikit-learn 0.22.1](https://scikit-learn.org/stable/)
- [opencv-contrib-python-headless 4.1.2.30](https://pypi.org/project/opencv-contrib-python-headless/)

### Getting Started

1. [Fork this repository](https://help.github.com/en/articles/fork-a-repo)
2. [Clone your forked repository](https://help.github.com/en/articles/fork-a-repo#step-2-create-a-local-clone-of-your-fork)
   - `git clone https://github.com/YOUR-USERNAME/food-tracker-bot.git`
   
### Project structure

```bash
.
├── chatbot                  # Chatbot module
│   ├── data                 # Some training data
│   └── main.py              # Main chatbot class
│
├── food_classifier          # Food classifier module
│   ├── k_model.py           # Used to build the keras model with some architectures to choose
│   ├── predict.py           # Script to obtain a prediction from an image
│   └── train.py             # Script to train the model
│
├── rasa                     # Unused module with rasa chatbot implementation
│   ├── data                 # Some training data
│   ├── models               # Trained models
│   ├── rasa-train.py        # Script to train rasa data
│   └── main.py              # Rasa in action!
│
├── utils                    # Some project utilities
│   ├── download_image.py    # Script to download and resize online image
│   └── generate_message.py  # Script to transform food tags to an end-user message
│
├── bot.py                   # Main bot class
│
└── mobilenet_model.h5       # Trained model using MobileNet
```
   
### Deployment

1. __Create the Telegram bot profile__

   To create the bot profile you can use an integrated Telegram bot called “Bot Father”. With this bot, you can create new bots by filling the name, description, image and commands. This bot will give you a token (```TELEGRAM_BOT_TOKEN```) that you have to use in the server to get all user info and messages. You have to add this token in the [_bot.py_](https://github.com/mcalvog/food-tracker-bot/blob/master/bot.py) file.

2. __Setup server__

   You can setup the bot server remotely or on a local machine. You only have to run the _bot.py_ file on the machine where you want to host the server with the command ```python3 bot.py```.
   
   After that, you have to tell Telegram API your server url (weebhook). To do that, you simply has to enter this website: ```https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}```. The url has to be __public__ and with a __SSL__ certificate (https). If you are using a local machine, you will have to make a tunnel to your local url (See: [NGROK](https://ngrok.com/) utility).
   
3. __Use the bot!__

   You are ready to use the bot :)
