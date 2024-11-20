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
    
    def writeJson(self, filename, data):    
        self.productsService.writeJson(filename, data)
    
    def upDateJson(self, filename, update):
        return self.productsService.updateJson(filename, update)
             
    def calcProfit(self, fileName, mYthrow):
        self.readJson(self, fileName)
        return self.result

    def getLabelResult(self):
        return self.result

    def getLabelNameFila(self, nameJson):
        dictData =  self.readJson(nameJson)
        return dictData['printerName']

    def createUser(self, printerName, dictUser):
        self.writeJson(printerName, dictUser)

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
                print(self.getID(PRINTERNAMEINDEX + f'{index}'))
            