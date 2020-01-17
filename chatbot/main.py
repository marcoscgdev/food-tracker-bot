import os
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# chatterbot - corpus

def train():
    chatbot = ChatBot("M2 ChatBot",
        storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
        logic_adapters = [{
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'Lo siento, no te he entendido.',
                'maximum_similarity_threshold': 0.7
            },
            {
                'import_path': "chatterbot.logic.MathematicalEvaluation"
            },
            {
                'import_path': 'chatterbot.logic.TimeLogicAdapter',
            }
        ],
        input_adapter = "chatterbot.input.TerminalAdapter",
        output_adapter = "chatterbot.output.TerminalAdapter",
        database_uri = 'sqlite:///database.sqlite3'
    )

    general_trainer = ChatterBotCorpusTrainer(chatbot)

    general_trainer.train(
        "chatterbot.corpus.spanish",
        "chatbot/data/conversation.yml",
        "chatbot/data/emociones.yml",
        "chatbot/data/greetings.yml",
        "chatbot/data/perfilbot.yml",
        "chatbot/data/psicologia.yml",
        "chatbot/data/trivia.yml",
        "chatbot/data/IA.yml"
    )

    return chatbot

def response(chatbot, text):
    # fix questions
    if text.endswith('?') and not text.startswith('¿'):
        text = "¿" + text;

    # fix exclamations
    if text.endswith('!') and not text.startswith('¡'):
        text = "¡" + text;

    return chatbot.get_response(text)
