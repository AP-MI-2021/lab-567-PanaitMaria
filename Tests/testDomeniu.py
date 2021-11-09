from Domain.vanzare import creeazaVanzare, getId, getTitlu, getGen, getPret, getReducere


def testVanzare():
    vanzare = creeazaVanzare("1", "Harry Potter", "fictiune", 30, "silver")

    assert getId(vanzare) == "1"
    assert getTitlu(vanzare) == "Harry Potter"
    assert getGen(vanzare) == "fictiune"
    assert getPret(vanzare) == 30
    assert getReducere(vanzare) == "silver"