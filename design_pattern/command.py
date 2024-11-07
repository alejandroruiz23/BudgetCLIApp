from abc import ABC, abstractmethod
from Domain.Cuenta import Transaction

class Command(ABC):
    @abstractmethod
    def execute(self)->None:
        pass

class SaveInvoice(Command):
    def __init__(self, transaction: Transaction, monto):
        self.transaction = transaction
        self.monto = monto

    def execute(self):
        self.transaction.addIngreso(self.monto)

class SaveExpense(Command):
    def __init__(self,transaction: Transaction, monto):
        self.monto = monto
        self.transaction = transaction

    def execute(self):
        self.transaction.addGasto(self.monto)
