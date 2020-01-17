from rasa_core.agent import Agent

agent = Agent.load('models/dialogue', interpreter='models/default/model_20200116-113644')

responses = agent.handle_message("hola")
for response in responses:
  print(response)
