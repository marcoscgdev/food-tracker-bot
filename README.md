# Food Tracker BOT
A simple an easy to use food tracker Telegram bot.

---

## About

Telegram bot that, based on the photos you send to, tells if you should improve or not your diet based on how healthy or unhealthy is the food you eat on a weekly basis. Users can also have a conversation with the bot as if it were a human.

## Developing

### Requirements

- [Python 3.6.1](https://www.python.org/downloads/release/python-361/)

### Getting Started

1. [Fork this repository](https://help.github.com/en/articles/fork-a-repo)
2. [Clone your forked repository](https://help.github.com/en/articles/fork-a-repo#step-2-create-a-local-clone-of-your-fork)
   - `git clone https://github.com/YOUR-USERNAME/food-tracker-bot.git`
   
### Project structure

```bash
.
├── chatbot                  # Chatbot module
│   ├── data                 # Some training data
│   ├── main.py              # Main chatbot class
│
├── rasa                     # Unused module with rasa chatbot implementation
│   ├── data                 # Some training data
│   ├── models               # Trained models
│   ├── rasa-train.py        # Script to train rasa data
│   └── main.py              # Rasa in action!
│
├── utils                    # Some project utilities
│   ├── download_image.py    # Script to download and resize online image
│   ├── generate_message.py  # Script to transform food tags to and end-user message
```
   
### Deployment
