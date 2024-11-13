from productsService.productsSerivce import ProductsService

class Products():
    def __init__(self):
       self.productsService = ProductsService
       self.result = 'TEST'


    def readJson(self, fileName):
        return self.productsService.readJson(fileName)
    
    def writeJson(self, filename, data, popMethod, popValueError):
        return self.productsService.writeJson(filename, data, popMethod, popValueError)
    
    def upDateJson(self, filename, update, popMethod, popValueError):
        return self.productsService.updateJson(filename, update, popMethod, popValueError)
             
    def calcProfit(self, fileName, mYthrow):
        self.readJson(self, fileName)
        return self.result

    def getLabelResult(self):
        return self.result

