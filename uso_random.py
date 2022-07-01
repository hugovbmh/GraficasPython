from tkinter import * # Librerias para el entorno grafico python
from tkinter.ttk import *
import random

premio=random.randint(1,3)# randint genera un numero entero entre a y b, ambos incluidos

def apostar(numero):
    if numero==premio:
        etiqueta.configure(text='Ganaste!!')
    else:
        etiqueta.configure(text='Lo siento Perdiste!!')

ventana=Tk()
ventana.title('Premio')

etiqueta=Label(ventana, text='que boton es el del premio?')
etiqueta.pack()# posicionando adecuadamente la variable etiqueta en la ventana(entorno grafico de python)

for boton in range(1,4):
    Button(text='Boton ' + str(boton), command=lambda x=boton: apostar(x)).pack(side=LEFT)
# se ejecutara la funcion apostar con el valor de la variable boton . y side=LEFT permite mostrar los
# botones en horizontal
ventana.mainloop() 