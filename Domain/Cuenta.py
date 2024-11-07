from persistence.DB2 import Db2

class Transaction:
    def __init__(self):
        self._saldo = 0
        self.transaction = Db2()
        self.transacInvoice = []
        self.transacExpense = []

    def getSaldo(self):
        return f"Su saldo actual es de {self._saldo}"
    
    '''def setSaldo(self,saldo):
        self._saldo = saldo
    '''
    
    def getIngreso(self):
        self.transacciones = self.transaction.showTransactions()
        self.transacInvoice = []
        for mov in self.transacciones:

            if "INGRESO" in mov[2]:
                self.newInvoice = [mov[1],mov[2]]
                self.transacInvoice.append(self.newInvoice)
                                
        return self.transacInvoice
    
   
    def getGasto(self):
        self.transacciones = self.transaction.showTransactions()
        self.transacExpense = []
        for mov in self.transacciones:

            if "GASTO" in mov[2]:
                self.newInvoice = [mov[1],mov[2]]
                self.transacExpense.append(self.newInvoice)
                                
        return self.transacExpense

    def addIngreso(self, monto:float):
        if monto<0:
            raise ValueError("Ingrese un valor mayor a 0")
        self.transaction.addMovement(monto,"INGRESO")
        self._saldo = self._saldo + monto
        #return self.getSaldo()
    
    def addGasto(self, monto:float):
        self._saldo = self._saldo - monto
        if self._saldo<0:
            raise ValueError("No puede sacar mas de lo que tiene")
        self.transaction.addMovement(monto,"GASTO")
        return self.getSaldo()
    
    def showMovements(self):

        return self.transaction.showTransactions()
    
    

        

