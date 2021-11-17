
def getNewSale(_id: str, _titlu: str, _gen: str, _pret: float, _tip_red_cl: str):
    sale = {
        'id': _id,
        'titlu': _titlu,
        'gen': _gen,
        'pret': _pret,
        'tip_red_cl': _tip_red_cl
        }

    return sale


def getId(sale):
    """
    Da id-ul unei vanzari
    :param sale: dictionar ce retine o vanzare
    :return: id-ul vanzarii
    """
    return sale["id"]


def getTitlu(sale):
    """
    Da titlul unei carti
    :param sale: dictionar ce retine o vanzare
    :return: titlul cartii
    """
    return sale["titlu"]


def getGen(sale):
    """
    Da genul unei carti
    :param sale: dictionar ce retine o vanzare
    :return: genul cartii
    """
    return sale["gen"]


def getPret(sale):
    """
    Da pretul unei carti
    :param sale: dictionar ce retine o vanzare
    :return: pretul cartii
    """
    return sale["pret"]


def getTipRedCl(sale):
    """
    Da tipul de reducere al unui client
    :param sale: dictionar ce retine o vanzare
    :return: tipul de reducere al unui client
    """
    return sale["tip_red_cl"]


def toString(sale):
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, TipRedCl: {}".format(
        getId(sale),
        getTitlu(sale),
        getGen(sale),
        getPret(sale),
        getTipRedCl(sale)
    )
