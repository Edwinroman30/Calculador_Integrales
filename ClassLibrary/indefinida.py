from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter.font import BOLD
from sympy import *

x=Symbol('x')

class AppIndefinida(Frame):
    def __init__(self, root=  None):
        super().__init__(root,width=650,height=500,background="#e6ffd1")
        self.root=root
        self.pack()
        self.createWidget()
        
    def setFuction(self,fuction):
        if(self.BoxText.focus_get()==self.BoxText):
            self.BoxText.insert(END,fuction)
            
    def clearTextInputAll(self):
        if(self.BoxText.focus_get()==self.BoxText):
            self.BoxText.delete(0,END)
        elif(self.BoxText1.focus_get()==self.BoxText1):
            self.BoxText1.delete(0,END)

    def ClerarAll(self):
        self.BoxText.delete(0,END) 
        self.BoxText1.delete(0,END)
        self.BoxText.focus() 

    def clearTextInputOne(self):
        if(self.BoxText.focus_get()==self.BoxText):
            contador=self.BoxText.get()
            contador=len(contador)
            contador-=1
            self.BoxText.delete(contador,END)
        elif(self.BoxText1.focus_get()==self.BoxText1):   
            contador=self.BoxText1.get()
            contador=len(contador)
            contador-=1
            self.BoxText1.delete(contador,END)

    ##--------------> Funcion para integrar<---------------------------------
    def integrar(self):
        try:
            if(self.BoxText.get()!=""):
                self.BoxText1.delete(0,END)
                self.BoxText1.insert(END,integrate(self.BoxText.get()))
                self.BoxText1.insert(END,"+ C")
            else:
                self.BoxText1.delete(0,END)
                self.BoxText1.insert(END,"Error..complete el campo.") 
        except SympifyError:
            self.BoxText1.insert(END,"Error")
    
    ##--------------> creación de los widget<---------------------------------
    def createWidget(self):
        self.box=Button(self,text="*",padx=19,pady=10,relief="solid",background = "#e8cae2",command=lambda:self.setFuction("*"))
        self.box.place(x=120,y=145)
        
        self.bo7=Button(self,text="÷",padx=19,pady=10,relief="solid",background = "#e8cae2",command=lambda:self.setFuction("/"))
        self.bo7.place(x=180,y=145)
        
        self.boDi=Button(self,text="+",padx=19,pady=10,relief="solid",background = "#e8cae2",command=lambda:self.setFuction("+"))
        self.boDi.place(x=240,y=145)
        
        self.boRe=Button(self,text="-",padx=19,pady=10,relief="solid",background = "#e8cae2",command=lambda:self.setFuction("-"))
        self.boRe.place(x=300,y=145)
        
        self.bo1=Button(self,text="1",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("1"))
        self.bo1.place(x=120,y=195)
        
        self.bo2=Button(self,text="2",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("2"))
        self.bo2.place(x=180,y=195)
        
        self.bo3=Button(self,text="3",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("3"))
        self.bo3.place(x=240,y=195)
        
        self.boLog=Button(self,text="Log",padx=12,pady=10,relief="solid",background ="#abd3e3",command=lambda:self.setFuction("log("))
        self.boLog.place(x=300,y=195)
        
        self.boSin=Button(self,text="sin",padx=12,pady=10,relief="solid",background ="#abd3e3",command=lambda:self.setFuction("sin("))
        self.boSin.place(x=360,y=195)
        
        self.boCos=Button(self,text="cos",padx=12,pady=10,relief="solid",background ="#abd3e3",command=lambda:self.setFuction("cos("))
        self.boCos.place(x=420,y=195)
        
        self.boTan=Button(self,text="tan",padx=12,pady=10,relief="solid",background ="#abd3e3",command=lambda:self.setFuction("tan("))
        self.boTan.place(x=480,y=195)
        
        self.bo4=Button(self,text="4",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("4"))
        self.bo4.place(x=120,y=245)
        
        self.bo5=Button(self,text="5",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("5"))
        self.bo5.place(x=180,y=245)
        
        self.bo6=Button(self,text="6",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("6"))
        self.bo6.place(x=240,y=245)
        
        self.boxVa=Button(self,text="x",padx=19,pady=10,relief="solid",background ="#abd3e3",command=lambda:self.setFuction("x"))
        self.boxVa.place(x=300,y=245)
        
        self.boCsc=Button(self,text="csc",padx=12,pady=10,relief="solid",background ="#abd3e3",command=lambda:self.setFuction("csc("))
        self.boCsc.place(x=360,y=245)
        
        self.boSec=Button(self,text="sec",padx=12,pady=10,relief="solid",background ="#abd3e3",command=lambda:self.setFuction("sec("))
        self.boSec.place(x=420,y=245)
        
        self.boCot=Button(self,text="cot",padx=12,pady=10,relief="solid",background ="#abd3e3",command=lambda:self.setFuction("cot("))
        self.boCot.place(x=480,y=245)
        
        self.bo7=Button(self,text="7",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("7"))
        self.bo7.place(x=120,y=295)
        
        self.bo8=Button(self,text="8",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("8"))
        self.bo8.place(x=180,y=295)
        
        self.bo9=Button(self,text="9",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("9"))
        self.bo9.place(x=240,y=295)
        
        self.bo7=Button(self,text="x^",padx=15,pady=10,relief="solid",background ="#abd3e3",command=lambda:self.setFuction("x**"))
        self.bo7.place(x=300,y=295)
        
        self.boPoten=Button(self,text="Limpiar\n todo",padx=61,pady=28,relief="solid",background="#f9f4af",command=self.ClerarAll)
        self.boPoten.place(x=360,y=295)
        
        self.bo0=Button(self,text="0",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("0"))
        self.bo0.place(x=120,y=345)
        
        self.boPunto=Button(self,text=".",padx=21,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("."))
        self.boPunto.place(x=180,y=345)
        
        self.boEliTodo=Button(self,text="AC",padx=14,pady=10,relief="solid",background="#f9f4af",command=self.clearTextInputAll)
        self.boEliTodo.place(x=240,y=345)
        
        self.boRaiz=Button(self,text="√",padx=18,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("sqrt("))
        self.boRaiz.place(x=300,y=345)
        
        self.boParen=Button(self,text="(",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction("("))
        self.boParen.place(x=120,y=395)
        
        self.boParent1=Button(self,text=")",padx=19,pady=10,relief="solid",background = "gray",command=lambda:self.setFuction(")"))
        self.boParent1.place(x=180,y=395)
        
        self.boPi=Button(self,text="π",padx=19,pady=10,relief="solid",background="#abd3e3",command=lambda:self.setFuction("pi"))
        self.boPi.place(x=240,y=395)
        
        self.bo7=Button(self,text="e",padx=19,pady=10,relief="solid",background="#abd3e3",command=lambda:self.setFuction("e("))
        self.bo7.place(x=300,y=395)
        
        self.boDel1=Button(self,text="DEL",padx=19,pady=10,relief="solid",background="#f9f4af",command=self.clearTextInputOne)
        self.boDel1.place(x=360,y=395)
        
        self.bointe=Button(self,text="Integrar",padx=23,pady=10,relief="solid",background="#0a729d",command=self.integrar)
        self.bointe.place(x=435,y=395)

        Label(self,text="Función",background="#e6ffd1",font=("verdana",8,BOLD)).place(x=120,y=10)
        Label(self,text="Resultado",background="#e6ffd1",font=("verdana",8,BOLD)).place(x=120,y=75)
        Label(self,text="Fun. Trigonométricas",background="#e6ffd1",font=("verdana",9,BOLD)).place(x=376,y=158)
        
        self.BoxText=Entry(self,relief="solid",justify='center',font="Arial 13")
        self.BoxText.place(x=120,y=40,width=410,height=30)
        self.BoxText.focus()
        
        self.BoxText1=Entry(self,relief="solid",justify='center',font="Arial 13")
        self.BoxText1.place(x=120,y=100,width=410,height=30)
        self.BoxText1.focus()





