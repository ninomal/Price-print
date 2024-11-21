from productsService.productsSerivce import ProductsService
import json

PRINTERNAMEINDEX = 'PRINTER'

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
        id = (self.getPrinterID() + 1)
        data.update({'ID': id}) 
        printerName = PRINTERNAMEINDEX + f'{id}'
        print(printerName, id)
        #self.writeJson(printerName, data)

    def checkExist(self, path):
        return self.productsService.checkFileExist(path)
        
    def getID(self, nameJson):
        dictData =  self.readJson(nameJson)
        return dictData['ID']

    def checkIndexName(self):
        for index in range(self.conts):
            if index > self.conts:
                self.conts += 10
            elif self.productsService.checkFileExist(PRINTERNAMEINDEX + f'{index}'):
                return self.getID(PRINTERNAMEINDEX + f'{index}')
            
    def getListPrintsNames(self):
        listNames = []
        for row in range(self.checkIndexName()):
            nameJson = PRINTERNAMEINDEX + f'{row}'
            listNames.append(self.getNamePrinter(nameJson)) 
        return listNames
    
    def getPrinterID(self):
        idIndex = self.checkIndexName()