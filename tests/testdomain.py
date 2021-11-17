from domain.vanzari2 import getNewSale, getId, getTitlu, getGen, getPret, getTipRedCl


def test_sale():
    sale = getNewSale("1", "Alchimistul", "Fictiune", 40, "silver")

    assert getId(sale) == "1"
    assert getTitlu(sale) == "Alchimistul"
    assert getGen(sale) == "Fictiune"
    assert getPret(sale) == 40
    assert getTipRedCl(sale) == "silver"
