#Crear programa que calcule IMC.
from tkinter import messagebox, Tk, Label, Entry, Button, Frame


def imc():
    p= int(peso.get())
    a= float(altura.get())
    indice= (p/(a*a))

    if indice == 0 or indice <18:
        messagebox.showinfo("Resultado", "Peso bajo.")
    elif indice == 18 or indice < 25:
        messagebox.showinfo("Resultado", "Usted tiene un peso normal")
    elif indice == 25 or indice <27:
        messagebox.showinfo("Resultado", "Usted padece sobrepeso")


ventana = Tk()
ventana.title("IMC")
ventana.geometry("400x200")
ventana.config(bg="pink")

vp = Frame(ventana)
vp.config(bg="pink")
vp.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
vp.rowconfigure(0, weight=1)

peso =int()
etiqueta_peso = Label(vp, text="Ingrese el peso: ")
etiqueta_peso.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), )

altura= float()
etiqueta_altura = Label(vp, text="Ingrese la altura")
etiqueta_altura.grid(row=4, column=1, padx=(10, 10), pady=(10, 10), )

enter_peso =""
peso = Entry(vp, width=7, textvariable=peso)
peso.grid(row=1, column=2)

enter_altura=""
altura = Entry(vp, width=7, textvariable=altura)
altura.grid(row=4, column=2)

boton = Button(vp, text="Calcular", command=imc, width=20)
boton.grid(row=5, column=1, padx=(10, 10), pady=(10, 10))


ventana.mainloop()



