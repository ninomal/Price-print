from productsService.productsSerivce import ProductsService

class Products():
    def __init__(self):
       self.productsService = ProductsService

    def readJson(self, filename, popValueError):
        return self.productsService.readJson(filename, popValueError)
    
    def writeJson(self, filename, data, popMethod, popValueError):
        return self.productsService.writeJson(filename, data, popMethod, popValueError)
    
    def upDateJson(self, filename, update, popMethod, popValueError):
        return self.productsService.updateJson(filename, update, popMethod, popValueError)
             
    def calcProfit(self, fileName, mYthrow):
        pass