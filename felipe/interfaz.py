from tkinter import * 
from PIL import Image, ImageTk

main= Tk()

main.geometry("800x500")

frame1=Frame(main)
frame1.pack(side="left")

frame2=Frame(main)
frame2.pack(side="right")

imagen = Image.open("\\Users\\Usuario\\OneDrive\\Escritorio\\felipe\\logo-bancolombia.png")
imagen = imagen.resize((400,120))
imagen = ImageTk.PhotoImage(imagen)
label = Label(image=imagen, bg="blue")
label.pack()
label.pack(side="left")

titulo=Label(frame2,text="Inicio Sesion",font=("Calibri",24))
titulo.pack()

nombre=Label(frame2,text="Usuario", font=("Calibri",15))
nombre.pack()

ingreso_nombre=Entry(frame2)
ingreso_nombre.pack()

contraseña=Label(frame2,text="Contraseña", font=("Calibri",15))
contraseña.pack()

ingreso_contraseña=Entry(frame2)
ingreso_contraseña.pack()

def sesion():
    print("","Sesion Iniciada")

boton= Button(main,text="INGRESAR",font= "Calibri 11",command=sesion)
boton.pack()
boton.pack(side= "right")



mainloop()