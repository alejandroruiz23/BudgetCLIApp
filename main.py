from presentation.menu import showMenu

if __name__=='__main__':
    flag  = True
    menu = showMenu()
    while flag:
        menu.showOption()
        option = int(input("Ingrese su selección: "))
        if option <= 0 or option >=7:
            flag = False
    
        menu.selectedOption(option)
    
