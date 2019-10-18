from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

class ModelManager(object):

    @staticmethod
    def load_exisiting_model(model_directory):
        metadata = Metadata.load(model_directory)
        interpreter = Interpreter.load(metadata, RasaNLUConfig('rasa_config.json'))
        return interpreter
