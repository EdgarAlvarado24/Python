from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
root.title("Medio de Transporte")
opcion = StringVar()
opcion.set(None)

Radiobutton(root, text="Moto", variable=opcion, value='Moto', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Carro",  variable=opcion, value='Carro', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Barco",  variable=opcion, value='Barco', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Avion",  variable=opcion, value='Avion', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()