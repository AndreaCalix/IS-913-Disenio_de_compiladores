import basic

while True:
		text = input('GRUPO_#5 > ')
		result, error = basic.run('<stdin>', text)

		if error: print(error.as_string())
		elif result: print(result)