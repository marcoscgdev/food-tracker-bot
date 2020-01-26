def generate_message(data):
	if 'fats' and 'dessert' in data:
		return "Ese postre no es sano, quizás deberías cambiarlo por una fruta."
	elif 'fats' in data or 'carbs' in data:
		return "Esa comida no es sana... ¡Es hora de cambiar esos hábitos!"
	elif 'protein' in data:
		return "Genial! Las proteínas son estupendas para nuestro cuerpo."
	elif 'helthy' in data:
		return "Buen trabajo! Tus hábitos de comida son estupendos."
	elif 'appetizer' in data:
		return "Un aperitivo de vez en cuando no te hará daño."
	else:
		return str(data)
