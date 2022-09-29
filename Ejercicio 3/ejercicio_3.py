#libreria necesaria para utilizar expresiones regulares en python
import re

#Esto es para abrir y leer un archivo
textfile = open('prueba.txt', 'r')
filetext = textfile.read()
textfile.close()

# Metodo para devolver secuencia de numeros 
matches = re.findall(r'([0-9]+)', filetext)
print(matches)
# Metodo para devolver los caracteres especiales
matches2 = re.findall(r'([@_!#$%^&*()<>?\/\|}{~:])+', filetext)
print(matches2)
# Metodo para devolver3 o más vocales repetidas
matches3 = re.findall(r'([aeiou]).*\1.*\1', filetext)
print(matches3)
# Metodo para devolver secuencia de números seguidos de letras
matches4 = re.findall(r'([0-9]+[a-zA-Z]+)', filetext)
print(matches4)

#esto es para escribir la salida de los match en un archivo
salida=open('salida.txt','w')

salida.write("IS-913 DISENIO DE COMPILADORES\n")
salida.write("---- SALIDA DEL DOCUMENTO CON EL RESPECTIVO MACTH ----\n")
salida.write("\nSecuencia de numeros: " + str(matches))
salida.write("\nCaracteres Especiales: " + str(matches2))
salida.write("\nVocales 3 o mas veces repetidas: " + str(matches3))
salida.write("\nSecuencia de numeros seguidos de letras: " + str(matches4))

salida.close



