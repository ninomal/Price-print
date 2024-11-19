from productsService.productsSerivce import ProductsService
import json
class Products():
    def __init__(self):
       self.productsService = ProductsService()
       self.result = 'TEST'

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
        print(dictData)
        return dictData['printerName']

    def createUser(self, printerName, dictUser):
        self.writeJson(printerName, dictUser)