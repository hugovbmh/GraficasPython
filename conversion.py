from tkinter import * #librerias para el entorno grafico python
from tkinter.ttk import *
from tkinter.messagebox import *

tc=3.4 #variable tipo de cambio
# creando la funcion cotizar
def Cotizar(*args):
    try:
        soles.set(int(dolares.get())*tc)
    except ValueError:
        showerror(title='Error', message='Solo numeros arabigos!!!')
        dolares.set('') #limpiar dolares

ventana=Tk() # Tk es la interfaz grafica de python
ventana.title("Dolares a Soles")

marco=Frame(ventana, padding="20 20 20 20")
marco.grid(column=0,row=0,sticky=(N,W,E,S))
# el sticky se usa para manejar las posiciones en el grid
#       N
#   W       E
#       S
dolares=StringVar()
soles=StringVar()

# creando el control textbox con la variable dolares
entrada=Entry (marco,width=7,textvariable=dolares)
entrada.grid(column=2,row=1,sticky=(W,E))

# creando la etiqueta soles con la variable soles
Label(marco,textvariable=soles).grid(column=2,row=2,sticky=(W,E))

# boton que va a ejecutar la funcion Cotizar
Button(marco,text="Cotizar",command=Cotizar).grid(column=3,row=3,sticky=W)

Label(marco,text="dolares").grid(column=3,row=1,sticky=W)
Label(marco,text="equivale a").grid(column=1,row=2,sticky=E)
Label(marco,text="soles").grid(column=3,row=2,sticky=W)

entrada.focus() # enfoque en el textbox entrada

ventana.bind('<Escape>',lambda x:ventana.destroy()) # bindeando la tecla Escape para cerrar la ventana
ventana.mainloop() # ejecutar ventana 