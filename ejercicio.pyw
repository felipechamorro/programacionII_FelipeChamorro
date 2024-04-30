import tkinter
from tkinter import *
from tkinter import messagebox

ventana = tkinter.Tk()
ventana.title = "Registro de usuario"
ventana.geometry("800x600")

ventana.resizable(True, True)

nombre = tkinter.Label(ventana, text="Nombre: ")
nombre.grid(row=2 ,column= 0,)
apellido = tkinter.Label(ventana, text="Apellido: ")
apellido.grid(row=4 ,column= 0)
edad = tkinter.Label(ventana, text="Edad: ")
edad.grid(row=6 ,column= 0)
direccion = tkinter.Label(ventana, text="Direccion: ")
direccion.grid(row=8 , column= 0)
celular = tkinter.Label(ventana, text="Telefono: ")
celular.grid(row=10 , column= 0)
sexo = tkinter.Label(ventana, text="Sexo: ")
sexo.grid(row=12 , column= 0)
ciudad= Label(ventana, text="Ciudad: ")
ciudad.grid(row=14 ,column= 0)



medidas1 = tkinter.Entry(ventana,width= 30)
medidas1.grid(row= 2, column= 1)
medidas2 = tkinter.Entry(ventana, width= 30)
medidas2.grid(row=4 ,column= 1)
medidas3 = tkinter.Entry(ventana, width= 30)
medidas3.grid(row=6 ,column= 1)
medidas4 = tkinter.Entry(ventana, width= 30)
medidas4.grid(row=8 , column= 1)
medidas5 = tkinter.Entry(ventana, width= 30)
medidas5.grid(row=10 , column= 1)




def obtener_seleccion():
    global valor
    valor = variable.get()
    
variable = tkinter.StringVar(value="Ninguno")
boton1 = Radiobutton(ventana, text="F", variable = variable,value="F", command=obtener_seleccion)
boton2 = Radiobutton(ventana, text="M",variable = variable, value="M", command=obtener_seleccion)

boton1.grid(row=12, column=1)
boton2.grid(row=12, column=2)

lista = Listbox(ventana, width=20,height=5, selectmode="multiple")
lista.grid(row=14, column= 1)



def ciudadd():

    global elemento
    ciud = lista.curselection()
    for index in ciud:
        elemento = lista.get(index)
        

ciudades = ["Bucaramanga", "Cartagena", "Sincelejo", "Medellin"]

for elemento in ciudades:
    lista.insert(tkinter.END, elemento)
    elemento = ""



def registro():
   N1 = medidas1.get()
   A2= medidas2.get()
   E3= medidas3.get()
   D4= medidas4.get()
   T5=  medidas5.get()
   obtener_seleccion()
   ciudadd()
   s6= valor
   c7 = elemento


   messagebox.showinfo("","NOMBRE: " + N1 + "\n" + "APELLIDO: " + A2 + "\n" + "EDAD: " + E3 + "\n" + "DIRECCION: " + D4 + "\n" + "TELEFONO: " + T5 + "\n" + "SEXO: " + s6 +"\n" + "CIUDAD: " + c7 )
   

registrar= Button(ventana, text="Registrar", command= registro)
registrar.grid(row=16, column=1)

ventana.mainloop()