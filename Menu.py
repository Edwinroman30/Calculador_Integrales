from os import close
from tkinter import *
import tkinter
#from matplotlib.pyplot import winter
from indefinida import AppIndefinida
from definida import AppDefinida

class Principal(Frame):
    def __init__(self, root=  None):
        super().__init__(root,width=500,height=400)
        self.root=root
        self.pack()
        self.createWidget()
    def Close1(self):
        root=Tk()
        AppIndefinida(root)
        root.mainloop()
        
    def Close2(self):
        root=Tk()
        AppDefinida(root)
        root.mainloop()
    def createWidget(self):
        Label(self,text="Integrar").place(x=250,y=45)
        self.B7=tkinter.Button(self,text="Indefinida",padx=50,pady=20,command=self.Close1)
        self.B7.place(x=70,y=120)
        self.B7=tkinter.Button(self,text="Definida",padx=50,pady=20,command=self.Close2)
        self.B7.place(x=300,y=120)
        

root=Tk()
app=Principal(root)
app.mainloop()


















