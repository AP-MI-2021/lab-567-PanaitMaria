from Domain.vanzare import toString, getTitlu, getGen, getPret, getReducere
from Logic.CRUD import adaugVanzare, stergVanzare, modifVanzare, getById
from Logic.functionalitati import aplicDiscount, modifGenDupaTitlu, pretMinimGen, ordonareListaDupaPret, \
    afisTitluriDupaGen


def printMenu():
    print("1. Adaugare vanzare")
    print("2. Sterge vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare reducere - gold, silver sau none")
    print("5. Modificarea genului pentru un titlu dat")
    print("6. Determinarea prețului minim pentru fiecare gen")
    print("7. Ordonarea vânzărilor crescător după preț")
    print("8. Afișarea numărului de titluri distincte pentru fiecare gen")
    print("u. Undo")
    print("r. redo")
    print("a. Afisare vanzare")
    print("x. Iesire")

def uiAdaugaVanzare(lista, undoList, redoList):
    try:
        undoList = []
        redoList = []
        id = input("Dati id-ul: ")
        titlu = input("Dati titlul: ")
        gen = input ("Dati genul: ")
        pret = float(input("Dati pretul:"))
        reducere = input("Dati reducere:")
        rezultat = adaugVanzare(id, titlu, gen, pret, reducere, lista, undoList, redoList)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergeVanzare(lista, undoList, redoList):
    try:
        undoList = []
        redoList = []
        id = input("Dati id-ul vanzarii de sters: ")
        rezultat = stergVanzare(id, lista, undoList, redoList)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaVanzare(lista, undoList, redoList):
    try:
        undoList = []
        redoList = []
        id = input("Dati id-ul: ")
        titlu = input("Dati titlul: ")
        gen = input("Dati genul: ")
        pret = float(input("Dati pretul:"))
        reducere = input("Dati reducere:")
        rezultat = modifVanzare(id, titlu, gen, pret, reducere, lista, undoList, redoList)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showAll(lista):
    for vanzare in lista:
        print(toString(vanzare))

def uiAplicDiscount(lista, undoList, redoList):
    try:
        rezultat = aplicDiscount(lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModifGenDupaTitlu(lista, undoList, redoList):
    titlu = input("Dati titlul: ")
    genNou = input("Dati genul nou: ")
    try:
        rezultat = modifGenDupaTitlu(lista, titlu, genNou)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiPretMinimGen(lista):
    try:
        listaN = pretMinimGen(lista)
        for gen in listaN:
            print("Genul {} are pretul minim: {}".format(gen, listaN[gen]))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiOrdonareListaDupaPret(lista, undoList, redoList):
    rezultat = ordonareListaDupaPret(lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat


def uiAfisTitluriDupaGen(lista):
    try:
        listaN = afisTitluriDupaGen(lista)
        for gen in listaN:
            if listaN[gen] != 1:
                print("Genul {} are {} titluri".format(gen, listaN[gen]))
            else:
                print("Genul {} are un singur titlu".format(gen))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def functieUndo(lista, undoList, redoList):
        redoList.append(lista)
        lista = undoList.pop()
        return lista

def functieRedo(lista, undoList, redoList):
        undoList.append(lista)
        lista = redoList.pop()
        return lista

def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaVanzare(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergeVanzare(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaVanzare(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiAplicDiscount(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiModifGenDupaTitlu(lista, undoList, redoList)
        elif optiune == "6":
            uiPretMinimGen(lista)
        elif optiune == "7":
            lista = uiOrdonareListaDupaPret(lista, undoList, redoList)
        elif optiune == "8":
            uiAfisTitluriDupaGen(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                lista = functieUndo(lista, undoList, redoList)
            else:
                print("nu se poate face undo")
        elif optiune == "r":
            if len(redoList) > 0:
                lista = functieRedo(lista, undoList, redoList)
            else:
                print("nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")