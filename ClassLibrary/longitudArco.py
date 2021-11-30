from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox as MessageBox
from sympy import diff,integrate,sqrt,symbols,init_printing,plotting
import matplotlib.pyplot as plt


x = symbols("x")
init_printing(use_unicode=True)

class LongArco(Frame):
    
    def __init__(self, root=  None):
        super().__init__(root,width=650,height=500,background="#F3F4ED")
        root.title("Calculador de longitud de arco (Aplicación de Integral)") 
        self.pack()
        self.createWidget()
    
    #Funcion para insertar caracteres.    
    def setFuction(self,caracter):
        if(self.tboxReciveFunction.focus_get()==self.tboxReciveFunction):
            self.tboxReciveFunction.insert(END,caracter)
        elif(self.tboxinferirorLim.focus_get()==self.tboxinferirorLim):
            self.tboxinferirorLim.insert(END,caracter)
        elif(self.tboxsuperiorLim.focus_get()==self.tboxsuperiorLim):
            self.tboxsuperiorLim.insert(END,caracter)
        
    def clearTextInputAll(self):
        self.tboxReciveFunction.delete(0,END)   
        self.tboxinferirorLim.delete(0,END)
        self.tboxsuperiorLim.delete(0,END)
        self.tboxResult.delete(0,END)
        
    def clearTextInputOne(self):
        contador=self.tboxReciveFunction.get()
        contador=len(contador)
        contador-=1
        self.tboxReciveFunction.delete(contador,END)

   
    def LengthOfGraph(self,funcionFX,infLim,supLim):
       
       try:
           if(self.boxValidation()):
            
            resultList = []
            
            #Derivada de la funcion:
            diferenciaFX = diff(funcionFX, x)
            
            #Funcion de la longitud de arco:
            funIntegral = sqrt(1 + (diferenciaFX)**2)
            
            #Aplicando la formula de longitud de arco (Integral):
            longArcoExpre = integrate(funIntegral,x)
    
            
            inf = longArcoExpre.subs(x,infLim)
            sup = longArcoExpre.subs(x,supLim)
                        
            longArcoNeta = sup-inf
            
            #(FunOriginal,DifFunOriginal,FunAIntegral,LimInferior,LimSuperior,ExpresionLongArco,calculoNeto)
            resultList.append(funcionFX)
            resultList.append(diferenciaFX)
            resultList.append(funIntegral)
            resultList.append((infLim,supLim))
            resultList.append(longArcoExpre)
            resultList.append(longArcoNeta.evalf())
            
            #print((sup-inf).evalf()) -> Para Debugear
            #print(resultList[-1]) -> Para Debugear
            
            self.tboxResult.insert(END, resultList[-1])
       except:
            MessageBox.showinfo(title="Información Importante:",message="Es posible que no halla escrito la función con la regla correspondiente. Por favor verifique la función ??") 


    def GraphFunction(self):
        
        if(self.boxValidation()):
            funcionFX = self.tboxReciveFunction.get()
            imagGrap = plotting.plot(funcionFX,(x,self.tboxinferirorLim.get(),self.tboxsuperiorLim.get()),show=False,title="Gráfica de f(x):")
            backend = imagGrap.backend(imagGrap)
            
            backend.process_series()
            #backend.fig.savefig('.\Graph01.png', dpi=300) -> En caso  de querer almacenar la grafica
            backend.show() 
               
    def boxValidation(self):
        
        isValid = True
        
        if(self.tboxinferirorLim.get() == "" or self.tboxsuperiorLim.get() == ""):
            
            result = MessageBox.askquestion(title="Límites Vacios", message="Por favor asegúrese de que todos los campos estén rellenos. \n Si no especifica, los limites por defecto estos serán [-1 , 1]. ¿Está de acuerdo con esta selección?")

            if(result == MessageBox.YES):
                self.tboxinferirorLim.insert(END,"1")
                self.tboxsuperiorLim.insert(END,"-1")
                isValid = True
            else:
                isValid = False
                MessageBox.showinfo(title="Información importante", message="OK, recuerde especificar los límites de integración :)")
            
            if(self.tboxReciveFunction.get() == ""):
                MessageBox.showerror(title="Error", message="Upss... lo sentimos, para poder integrar debe de indicar una función.")
                isValid = False

        return isValid


    def createWidget(self):
        
        self.bo7=Button(self,text="*",padx=19,pady=10, relief="solid", background = "#e8cae2", command=lambda:self.setFuction("*"))
        self.bo7.place(x=120,y=145)
        self.bo7=Button(self,text="÷",padx=19,pady=10, relief="solid", background = "#e8cae2", command=lambda:self.setFuction("/"))
        self.bo7.place(x=180,y=145)
        self.bo7=Button(self,text="+",padx=19,pady=10, relief="solid", background = "#e8cae2", command=lambda:self.setFuction("+"))
        self.bo7.place(x=240,y=145)
        self.bo7=Button(self,text="-",padx=19,pady=10, relief="solid", background = "#e8cae2", command=lambda:self.setFuction("-"))
        self.bo7.place(x=300,y=145)
        self.bo7=Button(self,text="1",padx=19,pady=10, fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction("1"))
        self.bo7.place(x=120,y=195)
        self.bo7=Button(self,text="2",padx=19,pady=10, fg="#F7F7F7", relief="solid",background = "gray",  command=lambda:self.setFuction("2"))
        self.bo7.place(x=180,y=195)
        self.bo7=Button(self,text="3",padx=19,pady=10, fg="#F7F7F7", relief="solid",background = "gray",  command=lambda:self.setFuction("3"))
        self.bo7.place(x=240,y=195)
        self.bo8=Button(self,text="Log",padx=12,pady=10,  relief="solid",background ="#FFC286", command=lambda:self.setFuction("log()"))
        self.bo8.place(x=300,y=195)
        self.bo8=Button(self,text="sin",padx=12,pady=10,  relief="solid",background ="#abd3e3", command=lambda:self.setFuction("sin()"))
        self.bo8.place(x=360,y=195)
        self.bo8=Button(self,text="cos",padx=12,pady=10,  relief="solid",background ="#abd3e3", command=lambda:self.setFuction("cos()"))
        self.bo8.place(x=420,y=195)
        self.bo8=Button(self,text="tan",padx=12,pady=10,  relief="solid",background ="#abd3e3", command=lambda:self.setFuction("tan()"))
        self.bo8.place(x=480,y=195)
        self.bo8=Button(self,text="4",padx=19,pady=10, fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction("4"))
        self.bo8.place(x=120,y=245)
        self.bo8=Button(self,text="5",padx=19,pady=10, fg="#F7F7F7", relief="solid",background = "gray",  command=lambda:self.setFuction("5"))
        self.bo8.place(x=180,y=245)
        self.bo8=Button(self,text="6",padx=19,pady=10, fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction("6"))
        self.bo8.place(x=240,y=245)
        self.bo8=Button(self,text="ln",padx=17,pady=10, relief="solid",background ="#FFC286", command=lambda:self.setFuction("ln()"))
        self.bo8.place(x=300,y=245)
        self.bo8=Button(self,text="csc",padx=12,pady=10, fg="#F7F7F7", relief="solid",background ="#66806A", command=lambda:self.setFuction("csc()"))
        self.bo8.place(x=360,y=245)
        self.bo8=Button(self,text="sec",padx=12,pady=10, fg="#F7F7F7",  relief="solid",background ="#66806A", command=lambda:self.setFuction("sec()"))
        self.bo8.place(x=420,y=245)
        self.bo8=Button(self,text="cot",padx=12,pady=10, fg="#F7F7F7",  relief="solid",background ="#66806A",  command=lambda:self.setFuction("cot()"))
        self.bo8.place(x=480,y=245)
        self.bo7=Button(self,text="7",padx=19,pady=10, fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction("7"))
        self.bo7.place(x=120,y=295)
        self.bo7=Button(self,text="8",padx=19,pady=10, fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction("8"))
        self.bo7.place(x=180,y=295)
        self.bo7=Button(self,text="9",padx=19,pady=10, fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction("9"))
        self.bo7.place(x=240,y=295)
        self.bo7=Button(self,text="x^",padx=15,pady=10, relief="solid", background = "#e8cae2", command=lambda:self.setFuction("**"))
        self.bo7.place(x=300,y=295)
        
        self.bo7=Button(self,text="Gráficar",padx=30,pady=35, fg="#F7F7F7", relief="solid",background = "gray", command=self.GraphFunction)
        self.bo7.place(x=360,y=295)
        
        Button(self,text="X",padx=19,pady=35,font=("verdana",8,BOLD), relief="solid", background = "#B4C6A6", command=lambda:self.setFuction("x")).place(x=479,y=295)
        
        self.bo7=Button(self,text="0",padx=19,pady=10, fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction("0"))
        self.bo7.place(x=120,y=345)
        self.bo7=Button(self,text=".",padx=21,pady=10, fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction("."))
        self.bo7.place(x=180,y=345)
        
        self.bo7=Button(self,text="π",padx=19,pady=10,  fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction("pi"))
        self.bo7.place(x=240,y=345)
        
        self.bo7=Button(self,text="e",padx=19,pady=10,  fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction("e"))
        self.bo7.place(x=240,y=395)
        
        self.bo7=Button(self,text="√",padx=18,pady=10, relief="solid", background = "#e8cae2", command=lambda:self.setFuction("sqrt()"))
        self.bo7.place(x=300,y=345)
        
        self.bo7=Button(self,text="(",padx=19,pady=10,  fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction("("))
        self.bo7.place(x=120,y=395)
        self.bo7=Button(self,text=")",padx=19,pady=10,  fg="#F7F7F7", relief="solid",background = "gray", command=lambda:self.setFuction(")"))
        self.bo7.place(x=180,y=395)
        
     
        

        
        self.bo7=Button(self,text="AC",padx=14,pady=10,  relief="solid",background = "#FFF1AF", command=self.clearTextInputAll)
        self.bo7.place(x=300,y=395) 
        
        self.bo7=Button(self,text="DEL",padx=19,pady=10, relief="solid",background = "#FFF1AF", command=self.clearTextInputOne)
        self.bo7.place(x=360,y=395)
    
        
        
        Label(self,text="Función para integrar:",font=("verdana",8,BOLD)).place(x=120,y=10)
        Label(self,text="Límite\nInferior:",font=("verdana",8,BOLD)).place(x=350,y=10)
        Label(self,text="Límite\nSuperior:",font=("verdana",8,BOLD)).place(x=450,y=10)
        Label(self,text="Resultado:",font=("verdana",8,BOLD)).place(x=120,y=75)
        Label(self,text="Fun. Trigonométricas:",font=("verdana",9,BOLD)).place(x=376,y=158)
        
        Label(self,text="Worked by: Edwin A. Roman").place(x=10,y=470)
        
        
        #?ReciveFunction
        self.tboxReciveFunction=Entry(self,font="Arial 13")
        self.tboxReciveFunction.place(x=120,y=40,width=200,height=30)
        self.tboxReciveFunction.focus()
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
        
        self.bo7=Button(self,text="¡Integrar!",padx=23,pady=10, relief="solid",background = "#FFF1AF", command= lambda: self.LengthOfGraph(self.tboxReciveFunction.get(),self.tboxsuperiorLim.get(),self.tboxinferirorLim.get()))
        self.bo7.place(x=435,y=395) 