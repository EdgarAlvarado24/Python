from tkinter import *
from tkinter import ttk

root = Tk()

monitor = Label(root, text='Lista de Personas')
monitor.pack()
Listbox = Listbox(root)
opcion = StringVar()
for item in ["Pepe", "Maria", "Pedro", "Juan", "Ruben", "Carlos", "Laura", "Ana", "Lorena"]:
    Listbox.insert(END, item)
Listbox.pack()
root.mainloop()