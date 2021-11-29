from os import close
from tkinter import *
import tkinter
#from matplotlib.pyplot import winter
from indefinida import AppIndefinida
from definida import AppDefinida
from FormLongitudArco import LongArco

class Principal(Frame):
    
    def __init__(self, root=  None):
        
        super().__init__(root,width=780,height=300)
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
        
    def Close3(self):
        root=Tk()
        LongArco(root)
        root.mainloop()
        
    def createWidget(self):
        Label(self,text="Elija opción que desea llevar a cabo:").place(x=300,y=45)
        
        self.B7=tkinter.Button(self,text="Indefinida",padx=50,pady=20,command=self.Close1)
        self.B7.place(x=70,y=120)
        
        self.B7=tkinter.Button(self,text="Definida",padx=50,pady=20,command=self.Close2)
        self.B7.place(x=300,y=120)
        
        B7=tkinter.Button(self,text="Longitud de Arco",padx=50,pady=20,command=self.Close3)
        B7.place(x=500,y=120)
    

root=Tk()
app=Principal(root)
app.mainloop()
