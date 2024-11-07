from Domain.Cuenta import Transaction
from design_pattern.command import SaveExpense, SaveInvoice

class showMenu:
    def __init__(self):
        self.transaction = Transaction()

    def showOption(self):
        print("Por favor seleccione una de las opciones del menú para avanzar")
        print("1. Guardar un nuevo ingreso")
        print("2. Guardar un nuevo gasto")
        print("3. Mostrar el saldo actual")
        print("4. Mostrar movimientos")
        print("5. Mostrar ingresos")
        print("6. Mostrar gastos")
        print("7. Salir")
    
    def selectedOption(self,option:int):

        match option:
            case 1:
                print("\n")
                monto = float(input("Digite el monto del ingreso: "))
                self.invoice = SaveInvoice(self.transaction, monto)
                self.invoice.execute()
                print("----------------------")
            case 2:
                print("\n")
                monto = float(input("Digite el monto del gasto: "))
                self.expense = SaveExpense(self.transaction, monto)
                self.expense.execute()
                print("----------------------")
            case 3:
                print("\n")
                print("----------------------")
                print(self.transaction.getSaldo())
                print("----------------------")
            case 4:
                print("\n")
                print("----------------------")
                print("Los movimientos realizados son:")
                for mov in self.transaction.showMovements():
                    print(mov)
                print("----------------------")
            case 5:
                print("\n")
                print("----------------------")
                print("Los movimiento de tipo Ingreso realizados son:")
                print(self.transaction.getIngreso())
                print("----------------------")
            case 6:
                print("\n")
                print("----------------------")
                print("Los movimientos de tipo Gasto realizados son:")
                print(self.transaction.getGasto())
                print("----------------------")