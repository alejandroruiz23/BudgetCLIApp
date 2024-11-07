import time


class Db2:
    def __init__(self):
        self._transactList = list()
        self.flag = 1

    
    def addMovement(self, cash, type):
        
        if cash == 0 and type == 0:
            return "No puede ingresar movimientos en 0"
        nuevoMovimiento = [self.flag,cash,type]
        self._transactList.append(nuevoMovimiento)
        
        self.flag = self.flag + 1
        
       
        return self._transactList
    

    def showTransactions(self):
        return self._transactList
    
    
