from domain.vanzari2 import getPret, getGen, getId
from logic.CRUD import addSale, getById
from logic.functionality import reducere, modifyGen, minimPriceGen, orderByPrice, titlesPerGen


def test_reducere():
    lista = []
    lista = addSale("1", "Alchimistul", "Fictiune", 40, "silver", lista)
    lista = addSale("2", "Moara cu noroc", "Nuvela psihologica", 30, "none", lista)
    lista = addSale("3", "Ion", "roman realist", 25, "gold", lista)
    lista = reducere(lista)

    assert getPret(getById("1", lista)) == 38
    assert getPret(getById("2", lista)) == 30
    assert getPret(getById("3", lista)) == 22.5

def test_modifyGen():
    lista = []
    lista = addSale("1", "Alchimistul", "Fictiune", 40, "silver", lista)
    lista = addSale("2", "Moara cu noroc", "Nuvela psihologica", 30, "none", lista)
    lista = addSale("3", "Ion", "Roman psihologic", 25, "gold", lista)
    lista = modifyGen("Ion", "Roman realist", lista)
    lista = modifyGen("Moara cu noroc", "Nuvela de analiza", lista)

    assert getGen(getById("3", lista)) == "Roman realist"
    assert getGen(getById("2", lista)) == "Nuvela de analiza"

def test_minimPriceGen():
    lista = []
    lista = addSale("1", "Alchimistul", "Roman psihologic", 40, "silver", lista)
    lista = addSale("2", "Moara cu noroc", "Nuvela psihologica", 30, "none", lista)
    lista = addSale("3", "Ion", "Roman psihologic", 25, "gold", lista)
    result = minimPriceGen(lista)

    assert result["Roman psihologic"] == 25
    assert result["Nuvela psihologica"] == 30

def test_orderByPrice():
    lista = []
    lista = addSale("1", "Alchimistul", "Roman psihologic", 40, "silver", lista)
    lista = addSale("2", "Moara cu noroc", "Nuvela psihologica", 25, "none", lista)
    lista = addSale("3", "Ion", "Roman psihologic", 30, "gold", lista)
    result = orderByPrice(lista)

    assert getId(result[0]) == "2"
    assert getId(result[1]) == "3"
    assert getId(result[2]) == "1"

def test_titlesPerGen():
    lista = []
    lista = addSale("1", "Alchimistul", "Roman psihologic", 40, "silver", lista)
    lista = addSale("2", "Moara cu noroc", "Nuvela psihologica", 25, "none", lista)
    lista = addSale("3", "Ion", "Roman psihologic", 30, "gold", lista)
    result = titlesPerGen(lista)

    assert result["Roman psihologic"] == 2
    assert result["Nuvela psihologica"] == 1