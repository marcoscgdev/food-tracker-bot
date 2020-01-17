import logging, io, json, warnings
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.agent import Agent
import spacy

from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu import config
from rasa_nlu.model import Trainer

logging.basicConfig(level="INFO")
warnings.filterwarnings('ignore')

#train
agent = Agent('data/domain.yml', policies=[KerasPolicy()])

agent.train(
        'data/stories.md',
        validation_split=0.0,
        max_history=3,
        epochs=400
);

agent.persist('models/dialogue');

#NLU

spacy.load("es_core_news_sm")

training_data = load_data('data/data_nlu.md')
pipeline= ["nlp_spacy", "tokenizer_spacy", "intent_featurizer_spacy", "intent_classifier_sklearn"]
trainer = Trainer(RasaNLUConfig(cmdline_args={"pipeline": pipeline, "language": "es_core_news_sm"}))
interpreter = trainer.train(training_data)
model_directory = trainer.persist('./models/')

print(model_directory)
