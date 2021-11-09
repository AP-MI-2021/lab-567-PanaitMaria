from Logic.CRUD import adaugVanzare
from Tests.allTests import runAllTests
from UI.command_line_console import runMenu2
from UI.console import runMenu

def aleg_meniu():
    print("1. Interfata 1")
    print("2. Interfata 2")
    print("x. Program incheiat")


def main():
    runAllTests()
    lista = []
    undoList = []
    redoList = []
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 55, "gold", lista, undoList, redoList)
    lista = adaugVanzare("2", "Tabloul", "mister", 37, "none", lista, undoList, redoList)
    lista = adaugVanzare("3", "Crima si pedeapsa", "clasica", 15, "silver", lista, undoList, redoList)
    while True:
        aleg_meniu()
        optiune = input("Alege interfata: ")
        if optiune == "1":
            runMenu(lista)
        elif optiune == "2":
            runMenu2(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune greasita! Reincercati!")


if __name__ == '__main__':
    main()