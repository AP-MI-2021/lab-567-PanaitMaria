from domain.vanzari2 import getId, getTitlu, getGen, getPret, getTipRedCl
from logic.CRUD import addSale, getById, deleteSale, modifySale


def test_addSale():
    lista=[]
    lista = addSale("1", "Alchimistul", "Fictiune", 40, "silver",lista)
    assert len(lista) == 1
    assert getId(getById("1",lista))=="1"
    assert getTitlu(getById("1",lista))=="Alchimistul"
    assert getGen(getById("1",lista))=="Fictiune"
    assert getPret(getById("1",lista))==40
    assert getTipRedCl(getById("1",lista))=="silver"

def test_deleteSale():
    lista = []
    lista = addSale("1", "Alchimistul", "Fictiune", 40, "silver", lista)
    lista = addSale("2", "Moara cu noroc", "Nuvela psihologica", 30, "none", lista)

    lista = deleteSale("1",lista)
    assert len(lista)==1
    assert getById("1",lista) is None
    assert getById("2", lista) is not None

    try:
        lista = deleteSale("100", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getById("2", lista) is not None
    except Exception:
        assert False

def test_modifySale():
    lista = []
    lista = addSale("1", "Alchimistul", "Fictiune", 40, "silver", lista)
    lista = addSale("2", "Moara cu noroc", "Nuvela psihologica", 30, "none", lista)

    lista = modifySale("1", "Ion", "roman realist", 25, "gold", lista)

    saleUpdate = getById("1", lista)
    assert getId(saleUpdate) == "1"
    assert getTitlu(saleUpdate) == "Ion"
    assert getGen(saleUpdate) == "roman realist"
    assert getPret(saleUpdate) == 25
    assert getTipRedCl(saleUpdate) == "gold"

    saleNewUpdate = getById("2", lista)
    assert getId(saleNewUpdate) == "2"
    assert getTitlu(saleNewUpdate) == "Moara cu noroc"
    assert getGen(saleNewUpdate) == "Nuvela psihologica"
    assert getPret(saleNewUpdate) ==30
    assert getTipRedCl(saleNewUpdate) == "none"

    lista = []
    lista = addSale("1", "Alchimistul", "Fictiune", 40, "silver", lista)
    lista = addSale("2", "Moara cu noroc", "Nuvela psihologica", 30, "none", lista)
    saleNewUpdate= getById("1", lista)
    assert getId(saleNewUpdate) == "1"
    assert getTitlu(saleNewUpdate) == "Alchimistul"
    assert getGen(saleNewUpdate) == "Fictiune"
    assert getPret(saleNewUpdate) == 40
    assert getTipRedCl(saleNewUpdate) =="silver"