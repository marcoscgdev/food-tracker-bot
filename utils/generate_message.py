def generate_message(data):
	if 'fats' and 'dessert' in data:
		return "Ese postre no es sano, quizás deberías cambiarlo por una fruta."
	elif 'fats' in data:
		return "Esa comida no es sana, ¿por qué no comes una ensalada?"
	elif 'protein' in data:
		return "Genial! Las proteínas son estupendas para nuestro cuerpo."
	elif 'helthy' in data:
		return "Buen trabajo! Estás comiendo sano."
	else:
		return str(data)
