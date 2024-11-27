from productsService.productsSerivce import ProductsService
import json

PRINTERNAMEINDEX = "PRINTER"

class Products():
    def __init__(self):
       self.productsService = ProductsService()
       self.result = 'TEST'
       self.id = 0
       self.conts = 15

    def readJson(self, fileName):
        return self.productsService.readJson(fileName)
    
    def writeJson(self, fileName, data):     
        self.productsService.writeJson(fileName, data)
    
    def upDateJson(self, filename, update):
        self.productsService.updateJson(filename, update)
             
    def calcProfit(self, fileName, mYthrow):
        self.readJson(self, fileName)
        return self.result

    def getLabelResult(self):
        return self.result

    def getNamePrinter(self, nameJson):
        dictData =  self.readJson(nameJson)
        return dictData['printerName']

    def createUser(self,  data):
        id = (self.checkIndexName())
        print(id)
        id +=1
        print(id)
        data.update({'ID': (id)}) 
        print(data)
        printerName = PRINTERNAMEINDEX + f"{(id -1)}" + ".json"
        print(printerName ,data)
        self.writeJson(printerName, data)

    def checkExist(self, path):
        return self.productsService.checkFileExist(path)
        
    def getID(self, nameJson):
        dictData =  self.readJson(nameJson)
        return dictData['ID']

    def checkIndexName(self):
        index = 0
        print(self.conts)
        for index in range(self.conts):
            if index >= (self.conts -1) and self.conts < 20: #need add dynamic for ID
                self.conts += 9
            elif self.productsService.checkFileExist(PRINTERNAMEINDEX + f"{(index)}" + ".json"):     
                self.id = index
        return self.id
            
    def getListPrintsNames(self):
        listNames = []
        for row in range(self.checkIndexName()):
            nameJson = PRINTERNAMEINDEX + f"{(row)}" + ".json"
            listNames.append(self.getNamePrinter(nameJson)) 
        return listNames
    
    def getPrinterID(self):
        idIndex = self.checkIndexName()