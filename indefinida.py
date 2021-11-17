from tkinter import *



class AppIndefinida(Frame):
    def __init__(self, root=  None):
        super().__init__(root,width=1000,height=400)
        self.root=root
        self.pack()
        self.createWidget()
        
    def setFuction(self,fuction):
        self.BoxText.insert(END,fuction)
    
    def clearTextInputAll(self):
        self.BoxText.delete(0,END)   
    
    def clearTextInputOne(self):
        contador=self.BoxText.get()
        contador=len(contador)
        contador-=1
        self.BoxText.delete(contador,END)   

    def createWidget(self):
        self.bo7=Button(self,text="7",padx=12,pady=10,command=lambda:self.setFuction("7"))
        self.bo7.place(x=70,y=120)
        
        self.bo8=Button(self,text="8",padx=12,pady=10,command=lambda:self.setFuction("8"))
        self.bo8.place(x=130,y=120)

        self.B9=Button(self,text="9",padx=12,pady=10,command=lambda:self.setFuction("9"))
        self.B9.place(x=190,y=120)
        
        self.Bdel=Button(self,text="DEL",padx=12,pady=10,command=self.clearTextInputOne)
        self.Bdel.place(x=250,y=120)

        self.Bac=Button(self,text="AC",padx=12,pady=10,command=self.clearTextInputAll)
        self.Bac.place(x=310,y=120)

        self.Bfx=Button(self,text="f(x)",padx=12,pady=10,command=lambda:self.setFuction("f(x)"))
        self.Bfx.place(x=370,y=120)

        self.Bx=Button(self,text="x",padx=12,pady=10,command=lambda:self.setFuction("x"))
        self.Bx.place(x=430,y=120)

        self.Bsin=Button(self,text="sin",padx=12,pady=10,command=lambda:self.setFuction("sin"))
        self.Bsin.place(x=490,y=120)

        self.B4=Button(self,text="4",padx=12,pady=10,command=lambda:self.setFuction("4"))
        self.B4.place(x=70,y=180)

        self.B5=Button(self,text="5",padx=12,pady=10,command=lambda:self.setFuction("5"))
        self.B5.place(x=130,y=180)

        self.B6=Button(self,text="6",padx=12,pady=10,command=lambda:self.setFuction("6"))
        self.B6.place(x=190,y=180)

        self.Bmas=Button(self,text="+",padx=16,pady=10,command=lambda:self.setFuction("+"))
        self.Bmas.place(x=250,y=180)

        self.Bemenos=Button(self,text="-",padx=16,pady=10,command=lambda:self.setFuction("-"))
        self.Bemenos.place(x=310,y=180)

        self.Bxala2=Button(self,text="x^2",padx=12,pady=10,command=lambda:self.setFuction("**2"))
        self.Bxala2.place(x=370,y=180)

        self.Bcos=Button(self,text="cos",padx=12,pady=10,command=lambda:self.setFuction("cos"))
        self.Bcos.place(x=430,y=180)

        self.Belevar=Button(self,text="^",padx=16,pady=10,command=lambda:self.setFuction("**"))
        self.Belevar.place(x=490,y=180)

        self.B1=Button(self,text="1",padx=12,pady=10,command=lambda:self.setFuction("1"))
        self.B1.place(x=70,y=240)

        self.B2=Button(self,text="2",padx=12,pady=10,command=lambda:self.setFuction("2"))
        self.B2.place(x=130,y=240)

        self.B3=Button(self,text="3",padx=12,pady=10,command=lambda:self.setFuction("3"))
        self.B3.place(x=190,y=240)


        self.Basterisco=Button(self,text="*",padx=12,pady=10,command=lambda:self.setFuction("*"))
        self.Basterisco.place(x=250,y=240)

        self.Badividir=Button(self,text="/",padx=12,pady=10,command=lambda:self.setFuction("/"))
        self.Badividir.place(x=310,y=240)


        self.BelevarAla3=Button(self,text="x^3",padx=12,pady=10,command=lambda:self.setFuction("**3"))
        self.BelevarAla3.place(x=370,y=240)

        self.BTang=Button(self,text="tan",padx=12,pady=10,command=lambda:self.setFuction("tan"))
        self.BTang.place(x=430,y=240)

        self.Braiz=Button(self,text="√",padx=16,pady=10,command=lambda:self.setFuction("sqrt()"))
        self.Braiz.place(x=490,y=240)


        self.B0=Button(self,text="0",padx=12,pady=10,command=lambda:self.setFuction("0"))
        self.B0.place(x=70,y=300)

        self.Bpunto=Button(self,text=".",padx=12,pady=10,command=lambda:self.setFuction("."))
        self.Bpunto.place(x=130,y=300)

        self.Bparentesis1=Button(self,text="(",padx=12,pady=10,command=lambda:self.setFuction("("))
        self.Bparentesis1.place(x=190,y=300)

        self.Bparentesis2=Button(self,text=")",padx=12,pady=10,command=lambda:self.setFuction(")"))
        self.Bparentesis2.place(x=250,y=300)

        self.Bigual=Button(self,text="π",padx=12,pady=10,command=lambda:self.setFuction("π"))
        self.Bigual.place(x=310,y=300)

        self.BPi=Button(self,text="e",padx=12,pady=10,command=lambda:self.setFuction("e"))
        self.BPi.place(x=370,y=300)

        self.Be=Button(self,text="Integrar",padx=46,pady=10)
        self.Be.place(x=430,y=300)
        
        self.BoxText=Entry(self,font="Arial 13")
        self.BoxText.place(x=120,y=40,width=360,height=30)
        
        self.BoxText1=Entry(self,font="Arial 13")
        self.BoxText1.place(x=120,y=83,width=360,height=30)
        





