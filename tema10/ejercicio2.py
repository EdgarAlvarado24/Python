from tkinter import *
from tkinter import ttk

root = Tk()

monitor = Label(root, text='Lista de Compras')
monitor.pack()

opcion = StringVar()
Checkbutton(root, text='Arroz', variable='Arroz', command=opcion).pack(anchor=W)
Checkbutton(root, text='Tomates', variable='Tomates', command=opcion).pack(anchor=W)
Checkbutton(root, text='Queso', variable='Queso', command=opcion).pack(anchor=W)
Checkbutton(root, text='Frutas', variable='Frutas', command=opcion).pack(anchor=W)

root.mainloop()