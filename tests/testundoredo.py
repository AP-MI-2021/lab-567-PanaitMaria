from domain.vanzari2 import getId
from logic.CRUD import addSale, getById


def testundoredo():
    redoList = []
    lista = []
    undoList = []

    rezultat = addSale("1", "Alchimistul", "Fictiune", 40, "silver", lista)
    undoList.append(lista)
    lista = rezultat
    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"

    rezultat = addSale("2", "Moara cu noroc", "Nuvela psihologica", 30, "none", lista)
    undoList.append(lista)
    lista = rezultat
    assert len(lista) == 2
    assert lista == [["1", "Alchimistul", "Fictiune", 40, "silver"], ["2", "Moara cu noroc", "Nuvela psihologica", 30, "none"]]

    rezultat = addSale("3", "Ion", "roman realist", 25, "gold", lista)
    undoList.append(lista)
    lista = rezultat

    assert len(lista) == 3

    redoList.append(lista)
    lista = undoList.pop()
    assert undoList == [[], [["1", "Alchimistul", "Fictiune", 40, "silver"]]]


    redoList.append(lista)
    lista = undoList.pop()
    assert undoList == [[]]

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == []

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == []


    rezultat = addSale("4", "Enigma Otiliei", "roman balzacian", 35, "none", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    rezultat = addSale("5", "Ultima noapte...", "roman al experientei", 50, "gold", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = addSale("6", "Baltagul", "roman mitic", 100, "asas", lista)
    undoList.append(lista)
    lista = rezultat

    assert len(lista) == 3

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 0


    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[], [["4", "Enigma Otiliei", "roman balzacian", 35, "none"]]]


    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[]]


    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 1

    if len(redoList) > 0:
        undoList.append(lista)
    lista = redoList.pop()
    assert len(redoList) == 0
    if len(undoList) > 0:
        redoList.append(lista)
    lista = undoList.pop()
    assert undoList == [[], [["4", "Enigma Otiliei", "roman balzacian", 35, "none"]]]

    if len(undoList) > 0:
        redoList.append(lista)
    lista = undoList.pop()
    assert undoList == [[]]

    rezultat = addSale("7", "Harap-Alb", "basm cult", 25, "silver", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()
    assert len(lista) == 2

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert undoList == [[], [["4", "Enigma Otiliei", "roman balzacian", 35, "none"]]]


    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == [[]]


    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    assert undoList == []


    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 1

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(lista) == 2


    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    assert len(redoList) == 0
