from domain.vanzari2 import toString
from logic.CRUD import addSale, deleteSale, modifySale
from logic.functionality import reducere, modifyGen, minimPriceGen, orderByPrice, titlesPerGen


def printMenu():
    print("1. Adaugare vanzare ")
    print("2. Stergere vanzare ")
    print("3. Modificare vanzare ")
    print("4. Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold. ")
    print("5. Modificarea genului unui titlu dat ")
    print("6. Determinarea prețului minim pentru fiecare gen.")
    print("7. Ordonarea vânzărilor crescător după preț.")
    print("8. Afișarea numărului de titluri distincte pentru fiecare gen.")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare vanzare ")
    print("X. Iesire")


def uiAddSale(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul ")
        titlu = input("Dati titlul ")
        gen = input("Dati genul ")
        pret = float(input("Dati pretul "))
        tip_red_cl = input("Dati tipul reducere client ")
        result = addSale(id, titlu, gen, pret, tip_red_cl, lista)
        undo_list.append(lista)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiDeleteSale(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul vanzarii pe care vreti sa o stergeti ")
        result = deleteSale(id,lista)
        undo_list.append(lista)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModifySale(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul vanzarii de modificat ")
        titlu = input("Dati noul titlu ")
        gen = input("Dati noul gen ")
        pret = float(input("Dati noul pret "))
        tip_red_cl = input("Dati noul tip de reducere client ")
        result = modifySale(id, titlu, gen, pret, tip_red_cl, lista)
        undo_list.append(lista)
        redo_list.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiReducere(lista, undo_list, redo_list):
    result = reducere(lista)
    undo_list.append(lista)
    redo_list.clear()
    return result

def uiModifyGen(lista, undo_list, redo_list):
    titlu = input("Dati un titlu ")
    gen = input("Dati noul gen ")
    result = modifyGen(titlu, gen, lista)
    undo_list.append(lista)
    redo_list.clear()
    return result

def uiMinimPriceGen(lista):
    result = minimPriceGen(lista)
    for gen in result:
        print("Genul {} are pretul minim {}". format(gen,result[gen]))

def uiOrderByPrice(lista):
    showAll(orderByPrice(lista))

def uiTitlesPerGen(lista):
    result = titlesPerGen(lista)
    for gen in result:
        print("Genul {} are {} titluri distincte".format(gen, result[gen]))

def showAll(lista):
    for sale in lista:
        print(toString(sale))


def runMenu(lista):
    undo_list = []
    redo_list = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune=="1":
            lista = uiAddSale(lista, undo_list, redo_list)
        elif optiune=="2":
            lista = uiDeleteSale(lista, undo_list, redo_list)
        elif optiune=="3":
            lista = uiModifySale(lista, undo_list, redo_list)
        elif optiune=="4":
            lista = uiReducere(lista, undo_list, redo_list)
        elif optiune=="5":
            lista = uiModifyGen(lista, undo_list, redo_list)
        elif optiune=="6":
            uiMinimPriceGen(lista)
        elif optiune=="7":
            uiOrderByPrice(lista)
        elif optiune=="8":
            uiTitlesPerGen(lista)
        elif optiune=="u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune=="a":
            showAll(lista)
        elif optiune=="x":
            break
        else:
            print("Optiune invalida! Reincercati!")