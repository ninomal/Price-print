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
        self.windows.geometry("845x430")
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
        self.enterPane = tk.Frame(self.windows, width=400, height=402,
                                   background="#4A1985")
        self.ioMainLoop()
        
    
    def firma(self):
        label_footer = tk.Label(self.windows, text="Radical dreamers aw rpg ltda", 
                        font=("Helvetica", 17), fg="#1b52a4", bg="#080121")
        label_footer.place(x=1, y=4, width=349, height=45)
           
    def frame1(self):
        self.anchorPane = tk.Frame(self.windows, width=400, height=160,
                                   background="#4A1985")
        self.anchorPane.place(x=15, y=260) 
        
    def canvasImage(self): 
        image_frame = Canvas(self.windows, width=400, height=400, background="#080121")
        image_frame.place(x=430, y=16)
        self.logo_img = PhotoImage(file= self.randomImagem())
        image_frame.create_image(200, 200, image = self.logo_img)
        
    def randomImagem(self):
        rng = random.Random()
        randInt = rng.randint(1, 2)
        path = Path(fr'ui\image\ess{randInt}.png')
        return path
                                                   
    def buttonPainel(self):
        buttonConfigs = tk.Button(self.anchorPane, text="Configs", font=("Helvetica", 18),
                               bg="#A580CA", command= self.tableConfigs)
        buttonConfigs.place(x=248, y= 5, width=149)
        buttonAdd = tk.Button(self.anchorPane, text="Add User", font=("Helvetica", 18),
                               bg="#A580CA", command= self.tableAddUser)
        buttonAdd.place(x=248, y= 57, width=149)

        buttonEnter = tk.Button(self.anchorPane, text="Enter", font=("Helvetica", 18),
                               bg="#A580CA", command= self.tableEnter)
        buttonEnter.place(x=248, y= 110, width=149)
        self.listOfComboInfo = [self.products.readJson('FLASHFORJE ADEVENTURE 5M PRO')]# need fix
        self.comboTabelas = ttk.Combobox(self.anchorPane, 
                                            values= self.listOfComboInfo,
                                            font=("Helvetica", 14),
                                             state='normal')
        self.comboTabelas.place(x=15, y=15, width=150, height=25)
        self.comboTabelas.set(self.listOfComboInfo[0])  

    def popADD(self):
        pass

    def popValueError(self):
        masterPoP = Tk()
        masterPoP.geometry("500x300")
        masterPoP.config(bg="#A580CA")
        messagebox = tk.Label(master= masterPoP,
                              text= "Value error",
                              font=("Helvetica", 27))
        messagebox.pack(padx= 40, pady= 40)   
        self.listData = []
        self.contsAdd = 0
                  
    def popEraserError(self):
        messagebox.showwarning(title="Erro",
                message= "Error para Adicionar")

    
    def popTabelaNoExist(self):
        messagebox.showwarning(title="Error",
                message= "Not exist")
        
    def popDataADD(self):
        messagebox.showwarning(title="Created",
                message= "object created")
     
                               
    def clearLIstEntrys(self):
        self.listData = []

    def destroy_label(self, labelPane):
        labelPane.destroy()

    def createUserJson(self, printerName, watts, filaType, priceFila):
        data = {'printerName': printerName, 'watts': watts, 'filaType':filaType,
                   'priceFila': priceFila }
        nameFile = printerName
        self.products.createUser(nameFile, data)
   
    def tableConfigs(self):
        configsPane = tk.Frame(self.windows, width=400, height=402,
                                   background="#4A1985")
        configsPane.place(x=15, y=15) 
        labelConfigs = tk.Label(master=configsPane, text='Configs',
                                background="#4A1985", font=("Helvetica", 20))
        labelConfigs.place(x= 90, y= 10)

        labelConfigs = tk.Label(master=configsPane, text='Select languagem:',
                                background="#4A1985", font=("Helvetica", 20))
        labelConfigs.place(x= 1, y= 75)

        self.listOfComboInfo = ['English'] # need ad list of languagem
        self.comboTabelas = ttk.Combobox(configsPane, 
                                            values= self.listOfComboInfo,
                                            font=("Helvetica", 15),
                                             state='normal')
        self.comboTabelas.place(x= 66, y=127, width=160, height=28)
        self.comboTabelas.set(self.listOfComboInfo[0])  

        buttonCreate= tk.Button(master = configsPane, text="Save", font=("Helvetica", 18),
                               bg="#A580CA", command= self.getCalc)
        buttonCreate.place(x=235, y= 346, width=149)

        buttonCreate= tk.Button(master = configsPane, text="Back", font=("Helvetica", 18),
                               bg="#A580CA", command= lambda: self.destroy_label(configsPane))
        buttonCreate.place(x=10, y= 346, width=146)

    
    def tableAddUser(self):
        addPane = tk.Frame(self.windows, width=400, height=402,
                                   background="#4A1985")
        addPane.place(x=15, y=15) 
        labelPrinte = tk.Label(master=addPane, text='Add new Printer',
                                background="#4A1985", font=("Helvetica", 20))
        labelPrinte.place(x= 90, y= 10)

        labelPrinter = tk.Label(master=addPane, text='Printer name:',
                                background="#4A1985", font=("Helvetica", 20))
        labelPrinter.place(x= 1, y= 100)
        entryPrinter = tk.Entry(master= addPane, width= 15, font=("Helvetica", 18))
        entryPrinter.place(x=188, y =105)
    
        labelWatt = tk.Label(master=addPane, text='Watt hour consumption:',
                                background="#4A1985", font=("Helvetica", 20))
        labelWatt.place(x= 1, y= 165)
        entryWatt = tk.Entry(master= addPane, width= 6, font=("Helvetica", 18))
        entryWatt.place(x=310, y =170)

        labelFilamentName = tk.Label(master=addPane, text='Filament type',
                                background="#4A1985", font=("Helvetica", 20))
        labelFilamentName.place(x= 1, y= 225)
        entryFilamentName = tk.Entry(master= addPane, width= 15, font=("Helvetica", 18))
        entryFilamentName.place(x=188, y =230)

        labelFilament = tk.Label(master=addPane, text='Filament cost:',
                                background="#4A1985", font=("Helvetica", 20))
        labelFilament.place(x= 1, y= 275)
        entryFilament = tk.Entry(master= addPane, width= 15, font=("Helvetica", 18))
        entryFilament.place(x=188, y =280)

        buttonCreate= tk.Button(master = addPane, text="Create", font=("Helvetica", 18),
                            bg="#A580CA", command= lambda: self.createUserJson(
                               entryPrinter.get(), entryWatt.get(), entryFilamentName.get(),
                               entryFilament.get()      
                            ))
        buttonCreate.place(x=235, y= 346, width=149)

        buttonCreate= tk.Button(master = addPane, text="Back", font=("Helvetica", 18),
                               bg="#A580CA", command= lambda: self.destroy_label(addPane))
        buttonCreate.place(x=10, y= 346, width=146)
       
    def tableEnter(self):
        self.enterPane.place(x=15, y=15) 
        nameOfPrinter = 'Flashforge Adventure 5m Pro' #self.products.readJson(self.comboTabelas, self.popValueError())
        labelPrinte = tk.Label(master=self.enterPane, text=f'Printer:\n {nameOfPrinter}',
                                background="#4A1985", font=("Helvetica", 20))
        labelPrinte.place(x= 5, y= 10)

        labelHours = tk.Label(master=self.enterPane, text='Hours:',
                                background="#4A1985", font=("Helvetica", 20))
        labelHours.place(x= 1, y= 110)
        entryHours = tk.Entry(master= self.enterPane, width= 6, font=("Helvetica", 18))
        entryHours.place(x=102, y =115)

        labelMinuts = tk.Label(master=self.enterPane, text='Minuts:',
                                background="#4A1985", font=("Helvetica", 20))
        labelMinuts.place(x= 200, y= 110)
        entryMinuts = tk.Entry(master= self.enterPane, width= 6, font=("Helvetica", 18))
        entryMinuts.place(x=302, y =115)
    
        labelweight = tk.Label(master=self.enterPane, text='Weight grams:',
                                background="#4A1985", font=("Helvetica", 20))
        labelweight.place(x= 1, y= 180)
        entryWeight = tk.Entry(master= self.enterPane, width= 15, font=("Helvetica", 18))
        entryWeight.place(x=185, y =185)

        labelPrice = tk.Label(master=self.enterPane, text='You Price:',
                                background="#4A1985", font=("Helvetica", 20))
        labelPrice.place(x= 1, y= 250)
        entryPrice = tk.Entry(master= self.enterPane, width= 15, font=("Helvetica", 18))
        entryPrice.place(x=185, y =255)

        labelNameFila = tk.Label(master=self.enterPane, text='Filment Type:',
                                background="#4A1985", font=("Helvetica", 20))
        labelNameFila.place(x= 1, y= 300)

        labelPrice = tk.Label(master=self.enterPane, text='Value:',
                                background="#4A1985", font=("Helvetica", 20))
        labelPrice.place(x= 1, y= 350)

        buttonEnter = tk.Button(master = self.enterPane, text="Calcule", font=("Helvetica", 18),
                               bg="#A580CA", command= self.getCalc)
        buttonEnter.place(x=235, y= 346, width=149)

    def getCalc(self):    
        nameFilament = self.products.getLabelNameFila()
        labelNameFila = tk.Label(master=self.enterPane, text= nameFilament,
                                background="#4A1985", font=("Helvetica", 20))
        labelNameFila.place(x= 185, y= 300)

        result = self.products.getLabelResult()
        labelResult= tk.Label(master=self.enterPane, text= result,
                                background="#4A1985", font=("Helvetica", 20))
        labelResult.place(x=80, y= 350)
    
    def ioMainLoop(self):
        self.windows.mainloop()
    
    
    