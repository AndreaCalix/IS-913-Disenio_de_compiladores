
from tkinter import *
from math import *
import tkinter as Calculadora
ventana=Tk()
ventana.geometry("360x320")
ventana.resizable(False,False)
ventana.title("calculadora")

index=0

data=Calculadora.Entry(ventana, font="Calibri 20")
data.grid(row=0,column=0, columnspan=5,padx=5, pady=5)

#BOTONES NUMEROS
button1=Calculadora.Button(ventana, text="1", width=8, height=3, bg='white',command=lambda: click(1)).grid(row=3,column=0,padx=3, pady=3)
button2=Calculadora.Button(ventana, text="2", width=8, height=3, bg='white',command=lambda: click(2)).grid(row=3,column=1,padx=3, pady=3)
button3=Calculadora.Button(ventana, text="3", width=8, height=3, bg='white',command=lambda: click(3)).grid(row=3,column=2,padx=3, pady=3)
button4=Calculadora.Button(ventana, text="4", width=8, height=3, bg='white',command=lambda: click(4)).grid(row=2,column=0,padx=3, pady=3)
button5=Calculadora.Button(ventana, text="5", width=8, height=3, bg='white',command=lambda: click(5)).grid(row=2,column=1,padx=3, pady=3)
button6=Calculadora.Button(ventana, text="6", width=8, height=3, bg='white',command=lambda: click(6)).grid(row=2,column=2,padx=3, pady=3)
button7=Calculadora.Button(ventana, text="7", width=8, height=3, bg='white',command=lambda: click(7)).grid(row=1,column=0,padx=3, pady=3)
button8=Calculadora.Button(ventana, text="8", width=8, height=3, bg='white',command=lambda: click(8)).grid(row=1,column=1,padx=3, pady=3)
button9=Calculadora.Button(ventana, text="9", width=8, height=3, bg='white',command=lambda: click(9)).grid(row=1,column=2,padx=3, pady=3)
button0=Calculadora.Button(ventana, text="0", width=8, height=3,bg='white',command=lambda: click(0)).grid(row=4,column=0,padx=3, pady=3)

#BOTONES OPERACIONES
buttonPoint=Calculadora.Button(ventana, text=".", width=8, height=3, bg='white', command=lambda: click(".")).grid(row=4,column=1,padx=3, pady=3)
buttonEqual=Calculadora.Button(ventana, text="=", width=8, height=3, bg='#b9bbbd', command=lambda: calculate()).grid(row=4,column=2,padx=3, pady=3)
buttonDel=Calculadora.Button(ventana, text="Borrar", width=8, height=3, command=lambda:delete()).grid(row=1,column=4,padx=3, pady=3)
buttonAdd=Calculadora.Button(ventana, text="+", width=8, height=3,command=lambda: click("+")).grid(row=1,column=3,padx=3, pady=3)
buttonSubtract=Calculadora.Button(ventana, text="-", width=8, height=3,command=lambda: click("-")).grid(row=2,column=3,padx=3, pady=3)
buttonMult=Calculadora.Button(ventana, text="x", width=8, height=3,command=lambda: click("x")).grid(row=3,column=3,padx=3, pady=3)
buttonDiv=Calculadora.Button(ventana, text="/", width=8, height=3,command=lambda: click("/")).grid(row=3,column=4,padx=3, pady=3)
buttonSqrt=Calculadora.Button(ventana, text="√", width=8, height=3,command=lambda: click("sqrt")).grid(row=2,column=4,padx=3, pady=3)
btnLeftBracket=Calculadora.Button(ventana, text="(", width=8, height=3, command=lambda: click("(")).grid(column=3, row=4,padx=3, pady=3)
btnRightBracket=Calculadora.Button(ventana, text=")", width=8, height=3, command=lambda: click(")")).grid(column=4, row=4,padx=3, pady=3)

#FUNCIONES
def delete():
	data.delete(0,END) 
	index=0

def click(bValue):
	global index
	data.insert(index,bValue)
	index+=4
	
def calculate():
	expression=data.get()
	expression2=expression.replace('x','*')
	print(expression2)
	try:
		result=eval(expression2)
		delete()
		data.insert(0,result)
		index=0
	except:
		print('formato invalido')

 

ventana.mainloop()

 