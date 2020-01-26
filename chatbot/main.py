import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import chatterbot.comparisons
import chatterbot.response_selection

# chatterbot - corpus

def train():
    chatbot = ChatBot("M2 ChatBot",
        storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
        logic_adapters = [{
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'RESPONSE_NOT_FOUND',
                'maximum_similarity_threshold': 0.7
            }
        ],
        input_adapter = 'chatterbot.input.TerminalAdapter',
        output_adapter = 'chatterbot.output.TerminalAdapter',
        database_uri = 'sqlite:///chatbot-database.sqlite3'
    )

    general_trainer = ChatterBotCorpusTrainer(chatbot)
    user_trainer = ListTrainer(chatbot) # for user inputs

    # Podriamos comparar si la base de datos ya existe para evitar entrenarlo de nuevo

    general_trainer.train(
        "chatterbot.corpus.spanish",
        "chatbot/data/emociones.yml",
        "chatbot/data/greetings.yml",
        "chatbot/data/perfilbot.yml",
        "chatbot/data/psicologia.yml"
    )

    return chatbot, user_trainer

def response(chatbot, text):
    return chatbot.get_response(text)
