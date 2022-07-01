#pip install -U ipykernel
'''
para generar un archivo de texto se tiene que instalar el ipykernel. para tal efecto
en la terminal del editor debes ejecutar:
pip install -U ipykernel
nota: ejecutar en la ruta donde esta su proyecto.
'''
from tkinter import *

# Almacenando en variables los datos ingresados en los controles textbox
def send_data():
    username_info=username.get()
    password_info=password.get()
    fullname_info=fullname.get()
    age_info=str(age.get())
    print(username_info,"\t",password_info,"\t",fullname_info,"\t",age_info) # "\t" salto tab
    
    # almacenando los datos en un archivo de texto
    file=open("user.text","a")# "w" solo agregara una fila de datos y el argumento "a" permite agregar varias filas
    file.write(username_info)
    file.write("\t")
    file.write(password_info)
    file.write("\t")
    file.write(fullname_info)
    file.write("\t")
    file.write(age_info)
    file.write("\t\n") # "\n" es salto de linea (enter)
    file.close() # cerrando el archivo
    print("Usuario Registrado. Username: {} | Fullname: {}".format(username_info,fullname_info ))

    # Limpiar los controles textbox
    username_entry.delete(0,END) #borrar desde posicion 0 hasta el final
    password_entry.delete(0,END)
    fullname_entry.delete(0,END)
    age_entry.delete(0,END)

# creando una nueva instancia de la clase Tk
ventana=Tk()
ventana.geometry("650x550") #tamaño de la ventana
ventana.title("Registrando Usuarios - Formulario - Python + Tkinter")
ventana.resizable(False,False) # la ventana no podra cambiar de tamaño
ventana.config(background="#7719AA") #color de fondo en hexadecimal

# Definir las etiquetas en el formulario. Use place para ubicar controles en el form
# Posicionando las etiquetas en el formulario
username_label=Label(text="Username",bg="#FFEEDD")
username_label.place(x=22,y=70)
password_label=Label(text="Password",bg="#FFEEDD")
password_label.place(x=22,y=130)
fullname_label=Label(text="Fullname",bg="#FFEEDD")
fullname_label.place(x=22,y=190)
age_label=Label(text="Age",bg="#FFEEDD")
age_label.place(x=22,y=250)

# Creando variables para Obtener y almacenar los datos de los usuarios
username=StringVar()
password=StringVar()
fullname=StringVar()
age=StringVar()

# Definir los textbox en el formulario.
username_entry=Entry(textvariable=username, width="40") #textbox
password_entry=Entry(textvariable=password, width="40", show="*") #cada vez q escriba aparecera en *
fullname_entry=Entry(textvariable=fullname, width="40")
age_entry=Entry(textvariable=age, width="40")

# Posicionando los controles textbox en el formulario
username_entry.place(x=22,y=100)
password_entry.place(x=22,y=160)
fullname_entry.place(x=22,y=220)
age_entry.place(x=22,y=280)

# Creando el boton submit

submit_btn=Button(ventana, text="Submit", width="30", height="2",command=send_data, bg="#00CD63")
submit_btn.place(x=22,y=320)
username_entry.focus_set()
ventana.mainloop()