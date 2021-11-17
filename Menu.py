from os import close
from tkinter import *
import tkinter
from matplotlib.pyplot import winter
from indefinida import AppIndefinida
from definida import AppDefinida

Window=tkinter.Tk()

Window.geometry("500x400")
Label(Window,text="Integrar").place(x=250,y=45)


def Close1():
    Window.destroy()
    root=Tk()
    AppIndefinida(root)
    root.mainloop()
    
def Close2():
    Window.destroy()
    root=Tk()
    AppDefinida(root)
    root.mainloop()

B7=tkinter.Button(Window,text="Indefinida",padx=50,pady=20,command=Close1)
B7.place(x=70,y=120)
B7=tkinter.Button(Window,text="Definida",padx=50,pady=20,command=Close2)
B7.place(x=300,y=120)


Window.mainloop()

















