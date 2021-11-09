from Logic.CRUD import adaugVanzare, stergVanzare
from UI.console import showAll


def oneLine(lista):
    while True:
        lineCom = input('Dati comenzile: ')
        lineCom = lineCom.split(';')
        for l in lineCom:
            l = l.split(',')
            if l[0] == 'add':
                if len(l) == 6:
                    try:
                        id = l[1]
                        titlu = l[2]
                        gen = l[3]
                        pret = float(l[4])
                        reducere = l[5]
                        lista = adaugVanzare(id, titlu, gen, pret, reducere, lista)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
                else:
                    print('Eroare: Numar invalid de parametrii')
            elif l[0] == "showall":
                showAll(lista)
            elif l[0] == 'delete':
                if len(l) == 2:
                    try:
                        id = l[1]
                        lista = stergVanzare(id, lista)
                    except ValueError as ve:
                        print(f'Eroare: {ve}')
                else:
                    print('Eroare: Numar invalid de parametrii')
            else:
                print('Comanda gresita! Reincercati!')


def printMeniu2():
    print("1. Adauga o vanzare/Sterge o vanzare/Arata toate vanzarile: ")
    print("x. Iesire")

def runMenu2(lista):
    while True:
        printMeniu2()
        optiune = input("Alegeti optiune: ")
        if optiune == "1":
            lista = oneLine(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")








