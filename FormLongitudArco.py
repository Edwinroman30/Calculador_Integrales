from tkinter import *
from tkinter.font import BOLD

#from sympy import *
from sympy import diff
from sympy import plot
from sympy import integrate
from sympy import sqrt
from sympy import symbols
from sympy import init_printing
from sympy import solve

x = symbols("x")
init_printing(use_unicode=True)

class LongArco(Frame):
    
    def __init__(self, root=  None):
        super().__init__(root,width=1000,height=500)
        self.pack()
        self.createWidget()
        
    def setFuction(self,caracter):
        self.tboxReciveFunction.insert(END,caracter)
    
    def clearTextInputAll(self):
        self.tboxReciveFunction.delete(0,END)   
    
    def clearTextInputOne(self):
        contador=self.tboxReciveFunction.get()
        contador=len(contador)
        contador-=1
        self.tboxReciveFunction.delete(contador,END)

   
    def LengthOfGraph(self,funcionFX,infLim,supLim):
        
        resultList = []
        
        #Derivada de la funcion:
        diferenciaFX = diff(funcionFX, x)
        
        #Funcion de la longitud de arco:
        funIntegral = sqrt(1 + (diferenciaFX)**2)
        
        #Aplicando la formula de longitud de arco (Integral):
        longArco = integrate(funIntegral,(x,supLim,infLim))
        
        #(FunOriginal,DifFunOriginal,FunAIntegral,LimInferior,LimSuperior,LongArco)
        resultList.append(funcionFX)
        resultList.append(diferenciaFX)
        resultList.append(funIntegral)
        resultList.append((infLim,supLim,))
        resultList.append(longArco)
        
        print(resultList[-1])
        self.tboxResult.insert(END, resultList[-1])
        plot(resultList[-1])


    
    def createWidget(self):
        
        self.bo7=Button(self,text="x",padx=19,pady=10,command=lambda:self.setFuction("*"))
        self.bo7.place(x=120,y=145)
        self.bo7=Button(self,text="÷",padx=19,pady=10,command=lambda:self.setFuction("/"))
        self.bo7.place(x=180,y=145)
        self.bo7=Button(self,text="+",padx=19,pady=10,command=lambda:self.setFuction("+"))
        self.bo7.place(x=240,y=145)
        self.bo7=Button(self,text="-",padx=19,pady=10,command=lambda:self.setFuction("-"))
        self.bo7.place(x=300,y=145)
        self.bo7=Button(self,text="1",padx=19,pady=10,command=lambda:self.setFuction("1"))
        self.bo7.place(x=120,y=195)
        self.bo7=Button(self,text="2",padx=19,pady=10,command=lambda:self.setFuction("2"))
        self.bo7.place(x=180,y=195)
        self.bo7=Button(self,text="3",padx=19,pady=10,command=lambda:self.setFuction("3"))
        self.bo7.place(x=240,y=195)
        self.bo8=Button(self,text="Log",padx=12,pady=10,command=lambda:self.setFuction("log()"))
        self.bo8.place(x=300,y=195)
        self.bo8=Button(self,text="sin",padx=12,pady=10,command=lambda:self.setFuction("sin()"))
        self.bo8.place(x=360,y=195)
        self.bo8=Button(self,text="cos",padx=12,pady=10,command=lambda:self.setFuction("cos()"))
        self.bo8.place(x=420,y=195)
        self.bo8=Button(self,text="tan",padx=12,pady=10,command=lambda:self.setFuction("tan()"))
        self.bo8.place(x=480,y=195)
        self.bo8=Button(self,text="4",padx=19,pady=10,command=lambda:self.setFuction("4"))
        self.bo8.place(x=120,y=245)
        self.bo8=Button(self,text="5",padx=19,pady=10,command=lambda:self.setFuction("5"))
        self.bo8.place(x=180,y=245)
        self.bo8=Button(self,text="6",padx=19,pady=10,command=lambda:self.setFuction("6"))
        self.bo8.place(x=240,y=245)
        self.bo8=Button(self,text="ln",padx=17,pady=10,command=lambda:self.setFuction("ln()"))
        self.bo8.place(x=300,y=245)
        self.bo8=Button(self,text="csc",padx=12,pady=10,command=lambda:self.setFuction("csc()"))
        self.bo8.place(x=360,y=245)
        self.bo8=Button(self,text="sec",padx=12,pady=10,command=lambda:self.setFuction("sec()"))
        self.bo8.place(x=420,y=245)
        self.bo8=Button(self,text="cot",padx=12,pady=10,command=lambda:self.setFuction("cot()"))
        self.bo8.place(x=480,y=245)
        self.bo7=Button(self,text="7",padx=19,pady=10,command=lambda:self.setFuction("7"))
        self.bo7.place(x=120,y=295)
        self.bo7=Button(self,text="8",padx=19,pady=10,command=lambda:self.setFuction("8"))
        self.bo7.place(x=180,y=295)
        self.bo7=Button(self,text="9",padx=19,pady=10,command=lambda:self.setFuction("9"))
        self.bo7.place(x=240,y=295)
        self.bo7=Button(self,text="x^",padx=15,pady=10,command=lambda:self.setFuction("x**"))
        self.bo7.place(x=300,y=295)
        
        self.bo7=Button(self,text="Gráficar",padx=60,pady=35,)
        self.bo7.place(x=360,y=295)
        
        self.bo7=Button(self,text="0",padx=19,pady=10,command=lambda:self.setFuction("0"))
        self.bo7.place(x=120,y=345)
        self.bo7=Button(self,text=".",padx=21,pady=10,command=lambda:self.setFuction("."))
        self.bo7.place(x=180,y=345)
        self.bo7=Button(self,text="AC",padx=14,pady=10,command=self.clearTextInputAll)
        self.bo7.place(x=240,y=345)
        self.bo7=Button(self,text="√",padx=18,pady=10,command=lambda:self.setFuction("sqrt()"))
        self.bo7.place(x=300,y=345)
        
        self.bo7=Button(self,text="(",padx=19,pady=10,command=lambda:self.setFuction("("))
        self.bo7.place(x=120,y=395)
        self.bo7=Button(self,text=")",padx=19,pady=10,command=lambda:self.setFuction(")"))
        self.bo7.place(x=180,y=395)
        self.bo7=Button(self,text="π",padx=19,pady=10,command=lambda:self.setFuction("pi"))
        self.bo7.place(x=240,y=395)
        self.bo7=Button(self,text="e",padx=19,pady=10,command=lambda:self.setFuction("e"))
        self.bo7.place(x=300,y=395)
        self.bo7=Button(self,text="DEL",padx=19,pady=10,command=self.clearTextInputOne)
        self.bo7.place(x=360,y=395)
    
        
        
        Label(self,text="Función").place(x=120,y=10)
        Label(self,text="Resultado").place(x=120,y=75)
        Label(self,text="Fun. Trigonométricas",font=("verdana",9,BOLD)).place(x=376,y=158)
        
        #?ReciveFunction
        self.tboxReciveFunction=Entry(self,font="Arial 13")
        self.tboxReciveFunction.place(x=120,y=40,width=200,height=30)
        #?
        
        #!Limites
        self.tboxsuperiorLim=Entry(self,font="Arial 13")
        self.tboxsuperiorLim.place(x=350,y=40,width=70,height=30)
        
        self.tboxinferirorLim=Entry(self,font="Arial 13")
        self.tboxinferirorLim.place(x=450,y=40,width=70,height=30)
        #!Limites
        
        
        self.tboxResult=Entry(self,font="Arial 13")
        self.tboxResult.place(x=120,y=100,width=398,height=40)
        
        #/////////////////////////////////////////////////////////////////////////////////////
        
        self.bo7=Button(self,text="¡Integrar!",padx=23,pady=10,command= lambda: self.LengthOfGraph(self.tboxReciveFunction.get(),self.tboxsuperiorLim.get(),self.tboxinferirorLim.get()))
        self.bo7.place(x=435,y=395)     
    



