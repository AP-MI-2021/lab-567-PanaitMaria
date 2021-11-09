from Domain.vanzare import getId
from Logic.CRUD import adaugVanzare, getById
from UI.console import functieUndo, functieRedo


def testUndoRedo():
    undoList = []
    redoList = []
    lista = []
    #adaugam 3 obiecte
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 15, "gold", lista, undoList, redoList)
    lista = adaugVanzare("2", "Tabloul", "mister", 20, "silver", lista, undoList, redoList)
    lista = adaugVanzare("3", "Crima si pedeapsa", "clasica", 30, "silver", lista, undoList, redoList)

    #undo 1
    if len(undoList) > 0:
        lista = functieUndo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById("3", lista) is None

    #undo 2
    if len(undoList) > 0:
        lista = functieUndo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById("2", lista) is None

    #undo 3
    if len(undoList) > 0:
        lista = functieUndo(lista, undoList, redoList)
    assert len(lista) == 0
    assert lista == []

    #undo 4 - nu face nimic
    if len(undoList) > 0:
        lista = functieUndo(lista, undoList, redoList)
    assert len(lista) == 0
    assert lista == []

    #adaugam alte 3 obiecte
    lista = adaugVanzare("1", "Great Gatsby", "clasica", 15, "gold", lista, undoList, redoList)
    lista = adaugVanzare("2", "Tabloul", "mister", 20, "silver", lista, undoList, redoList)
    lista = adaugVanzare("3", "Crima si pedeapsa", "clasica", 30, "silver", lista, undoList, redoList)

    #redo - nu face nimic
    if len(redoList) > 0:
        lista = functieRedo(lista, undoList, redoList)
    assert len(lista) == 3
    assert getId(getById("1", lista)) == "1"

    #undo 1
    if len(undoList) > 0:
        lista = functieUndo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById("3", lista) is None

    #undo 2
    if len(undoList) > 0:
        lista = functieUndo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById("2", lista) is None

    #redo 1
    if len(redoList) > 0:
        lista = functieRedo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById("2", lista) is not None

    #redo 2
    if len(redoList) > 0:
        lista = functieRedo(lista, undoList, redoList)
    assert len(lista) == 3
    assert getById("3", lista) is not None

    #undo 1
    if len(undoList) > 0:
        lista = functieUndo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById("3", lista) is None

    #undo 2 (14)
    if len(undoList) > 0:
        lista = functieUndo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById("2", lista) is None

    #adaug obiectul 4
    lista = adaugVanzare("4", "Dune", "SF", 60, "gold", lista, undoList, redoList)

    #redo - nu face nimic
    if len(redoList) > 0:
        lista = functieRedo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getId(getById("4", lista)) == "4"

    #undo 1
    if len(undoList) > 0:
        lista = functieUndo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById("4", lista) is None

    #undo 2
    if len(undoList) > 0:
        lista = functieUndo(lista, undoList, redoList)
    assert len(lista) == 0
    assert getById("1", lista) is None

    #redo 1
    if len(redoList) > 0:
        lista = functieRedo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById("1", lista) is not None

    #redo 2
    if len(redoList) > 0:
        lista = functieRedo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById("4", lista) is not None

    #redo - nu face nimic
    if len(redoList) > 0:
        lista = functieRedo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getId(getById("1", lista)) == "1"
    assert getId(getById("4", lista)) == "4"

































