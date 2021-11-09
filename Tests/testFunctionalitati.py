from Domain.vanzare import getPret, getGen, getId
from Logic.CRUD import adaugVanzare, getById
from Logic.functionalitati import aplicDiscount, modifGenDupaTitlu, pretMinimGen, ordonareListaDupaPret, \
    afisTitluriDupaGen


def testAplicDiscount():
    undoList = []
    redoList = []
    lista = []
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 15, "gold", lista, undoList, redoList)
    lista = adaugVanzare("2", "Tabloul", "mister", 20, "silver", lista, undoList, redoList)

    lista = aplicDiscount(lista)

    assert getPret(getById("1", lista)) == 13.5
    assert getPret(getById("2", lista)) == 19


def testModifGenDupaTitlu():
    undoList = []
    redoList = []
    lista = []
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 15, "gold", lista, undoList, redoList)
    lista = adaugVanzare("2", "Tabloul", "mister", 20, "silver", lista, undoList, redoList)

    titlu = "Tabloul"
    genNou = "crima"

    lista = modifGenDupaTitlu(lista, titlu, genNou)

    assert getGen(getById("2", lista)) == genNou
    assert getGen(getById("1", lista)) == "clasica"


def testPretMinimGen():
    undoList = []
    redoList = []
    lista = []
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 15, "gold", lista, undoList, redoList)
    lista = adaugVanzare("2", "Tabloul", "mister", 20, "silver", lista, undoList, redoList)
    lista = adaugVanzare("3", "Crima si pedeapsa", "clasica", 30, "silver", lista, undoList, redoList)

    listaN = pretMinimGen(lista)

    assert len(listaN) == 2
    assert listaN["clasica"] == 15

def testOrdonareListaDupaPret():
    undoList = []
    redoList = []
    lista = []

    lista = adaugVanzare("1", "Great Gatsby", "clasica", 20, "gold", lista, undoList, redoList)
    lista = adaugVanzare("2", "Tabloul", "mister", 15, "silver", lista, undoList, redoList)
    lista = adaugVanzare("3", "Crima si pedeapsa", "clasica", 30, "silver", lista, undoList, redoList)

    lista = ordonareListaDupaPret(lista)

    assert getId(lista[0]) == "2"
    assert getId(lista[1]) == "1"
    assert getId(lista[2]) == "3"


def testAfisTitluriDupaGen():
    undoList = []
    redoList = []
    lista = []
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 15, "gold", lista, undoList, redoList)
    lista = adaugVanzare("2", "Tabloul", "mister", 20, "silver", lista, undoList, redoList)
    lista = adaugVanzare("3", "Crima si pedeapsa", "clasica", 30, "silver", lista, undoList, redoList)
    lista = adaugVanzare("4", "Crima si pedeapsa", "clasica", 30, "gold", lista, undoList, redoList)

    listaN = afisTitluriDupaGen(lista)

    assert len(listaN) == 2
    assert listaN["clasica"] == 2
    assert listaN["mister"] == 1

