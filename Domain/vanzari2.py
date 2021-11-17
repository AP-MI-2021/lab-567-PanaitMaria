def getNewSale(_id: str, _titlu: str, _gen: str, _pret: float, _tip_red_cl: str):

    lista_vanzare = [_id, _titlu, _gen, _pret, _tip_red_cl]

    return lista_vanzare


def getId(lista_vanzare):
    """
    Da id-ul unei vanzari
    :param lista_vanzare: lista ce retine o vanzare
    :return: id-ul vanzarii
    """
    return lista_vanzare[0]


def getTitlu(lista_vanzare):
    """
    Da titlul unei carti
    :param lista_vanzare: lista ce retine o vanzare
    :return: titlul cartii
    """
    return lista_vanzare[1]


def getGen(lista_vanzare):
    """
    Da genul unei carti
    :param lista_vanzare: lista ce retine o vanzare
    :return: genul cartii
    """
    return lista_vanzare[2]


def getPret(lista_vanzare):
    """
    Da pretul unei carti
    :param lista_vanzare: lista ce retine o vanzare
    :return: pretul cartii
    """
    return lista_vanzare[3]


def getTipRedCl(lista_vanzare):
    """
    Da tipul de reducere al unui client
    :param lista_vanzare: lista ce retine o vanzare
    :return: tipul de reducere al unui client
    """
    return lista_vanzare[4]


def toString(lista_vanzare):
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, TipRedCl: {}".format(
        getId(lista_vanzare),
        getTitlu(lista_vanzare),
        getGen(lista_vanzare),
        getPret(lista_vanzare),
        getTipRedCl(lista_vanzare)
    )
