from tkinter import *
from tkinter import ttk

def reset():
    select.set(None)

root = Tk()
root.title("Ejercicio 1")

mainframe = ttk.Frame(root, padding="5 5 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

select = StringVar()
rButton1 = ttk.Radiobutton(mainframe, text="Opción 1", value=1, variable=select).grid(column=0, row=0, sticky=W)
rButton2 = ttk.Radiobutton(mainframe, text="Opción 2", value=2, variable=select).grid(column=0, row=1, sticky=W)
rButton3 = ttk.Radiobutton(mainframe, text="Opción 3", value=3, variable=select).grid(column=0, row=2, sticky=W)

ttk.Button(mainframe, text="Reiniciar", command=reset).grid(column=1, row=1, sticky=W)

root.mainloop()