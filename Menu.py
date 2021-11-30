from os import close
from tkinter import *
import tkinter
from tkinter.font import BOLD, ITALIC, families
from matplotlib.pyplot import winter
from sympy.utilities.iterables import rotations
from ClassLibrary.indefinida import AppIndefinida
from ClassLibrary.definida import AppDefinida
from ClassLibrary.longitudArco import LongArco

from PIL import ImageTk, Image

class Principal(Frame):
    def __init__(self, root=  None):
        super().__init__(root,width=650,height=500,background="#e6ffd1")
        self.root=root
        self.pack()
        self.createWidget()
    def Close1(self):
        root=Tk()
        AppIndefinida(root)
        root.eval( 'tk::PlaceWindow . center')
        root.mainloop()
        
    def Close2(self):
        root=Tk()
        AppDefinida(root)
        root.eval( 'tk::PlaceWindow . center')
        root.title("Integrales definidas")
        root.iconbitmap("./Img/Logo.ico")
        root.resizable(0,0)
        root.mainloop()
        
    def Close3(self):
        root=Tk()
        LongArco(root)
        root.eval( 'tk::PlaceWindow . center')
        root.title("Longitud del arco ")
        root.iconbitmap("./Img/Logo.ico")
        root.resizable(0,0)
        root.mainloop()
    def createWidget(self):
        Label(self,text="Cálculo Integral",font=("verdana",15,BOLD,ITALIC),background="#e6ffd1").place(x=250,y=20)
        Label(self,text="Seleccione su integral:",font=("verdana",12,BOLD,ITALIC),background="#e6ffd1").place(x=250,y=260)
        
        self.B7=tkinter.Button(self,text="Indefinida",padx=30,pady=20,relief="solid",bg="#20a6d8",
        font=("verdana",8,BOLD,ITALIC),command=self.Close1)
        self.B7.place(x=60,y=310)
        
        self.B7=tkinter.Button(self,text="Definida",relief="solid",bg="#20dbd8",
        font=("verdana",8,BOLD,ITALIC),padx=30,pady=20,command=self.Close2)
        self.B7.place(x=260,y=310)
        
        self.B7=tkinter.Button(self,text="Longitud del\narco",relief="solid",
        font=("verdana",8,BOLD,ITALIC),padx=20,pady=13,bg="#acedeb",command=self.Close3)
        self.B7.place(x=455,y=310)
        

root=Tk()
app=Principal(root)
root.iconbitmap("./Img/Logo.ico")
root.title("Cálculo Integral")
ima1=ImageTk.PhotoImage(Image.open("./Img/diseño.ico"))
Label(root,image=ima1,bg="#e6ffd1").place(x=150,y=100)

ima2=ImageTk.PhotoImage(Image.open("./Img/diseño1.ico"))
Label(root,image=ima2,bg="#e6ffd1").place(x=400,y=100)

root.eval( 'tk::PlaceWindow . center') #Esto es un codigo ..jjaaj...para centrar la ventana..
root.resizable(0,0)
app.mainloop()

