import basic

#tendra un bluce infinito que leera la entrada sin procesar desde la ventana de la terminal
while True:
    text = input('basic > ')
    result, error = basic.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)