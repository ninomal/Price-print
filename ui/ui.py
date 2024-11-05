import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pathlib import Path
from tkinter import filedialog
from products.products import Products
from pathlib import Path
import random


class Ui():
    def __init__(self):
        self.windows = Tk()
        self.windows.geometry("850x420")
        self.windows.title("3D PRICE")
        self.windows.config(background="#080121")
        self.caminhoEntry = ''
        self.conts = 0
        self.products = Products()
        self.firma()
        self.canvasImage()
        self.frame1()
        self.buttonPainel()
        self.clearLIstEntrys()
        self.ioMainLoop()

        
    def firma(self):
        label_footer = tk.Label(self.windows, text="Radical dreamers aw rpg ltda", 
                        font=("Helvetica", 17), fg="#1b52a4", bg="#080121")
        label_footer.place(x=1, y=10, width=349, height=45)
           
    def frame1(self):
        self.anchorPane = tk.Frame(self.windows, width=400, height=276,
                                   background="#4A1985")
        self.anchorPane.place(x=15, y=135) 
        
    def canvasImage(self): 
        image_frame = Canvas(self.windows, width=406, height=400, background="#080121")
        image_frame.place(x=430, y=8)
        self.logo_img = PhotoImage(file= self.randomImagem())
        image_frame.create_image(100, 100, image = self.logo_img)
        
    def randomImagem(self):
        rng = random.Random()
        randInt = rng.randint(1, 5)
        path = Path(fr"ui\image\ess{randInt}.png")
        print(path)
        return path
                                                   
    def buttonPainel(self):
        buttonConfigs = tk.Button(self.anchorPane, text="Configs", font=("Helvetica", 18),
                               bg="#A580CA", command= self.popADD)
        buttonConfigs.place(x=248, y= 124, width=149)
        buttonAdd = tk.Button(self.anchorPane, text="Add User", font=("Helvetica", 18),
                               bg="#A580CA", command= self.popADD)
        buttonAdd.place(x=248, y= 174, width=149)

        buttonEnter = tk.Button(self.anchorPane, text="Enter", font=("Helvetica", 18),
                               bg="#A580CA", command= self.popADD)
        buttonEnter.place(x=248, y= 224, width=149)

    def popADD(self):
        pass

    def popValueError(self):
        masterPoP = Tk()
        masterPoP.geometry("500x300")
        masterPoP.config(bg="#A580CA")
        messagebox = tk.Label(master= masterPoP,
                              text= "Valor invalido",
                              font=("Helvetica", 27))
        messagebox.pack(padx= 40, pady= 40)   
        self.listData = []
        self.contsAdd = 0
                  
    def popEraserError(self):
        messagebox.showwarning(title="Erro",
                message= "Error para Adicionar")
    
    def popPathError(self):
        messagebox.showwarning(title="Erro",
                message= "Erro de caminho")
        
    def popTabelaExist(self):
        messagebox.showwarning(title="Erro",
                message= "Tabela existe utilize outro nome")
    
    def popTabelaNoExist(self):
        messagebox.showwarning(title="Erro",
                message= "Nome da Tabela Não encontrada ")
        
    def popDataADD(self):
        messagebox.showwarning(title="Adicionada",
                message= "Os dados foram adicionados")
     
                               
    def clearLIstEntrys(self):
        self.listData = []
  
    
    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    