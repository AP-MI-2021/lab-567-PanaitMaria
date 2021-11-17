from domain.vanzari2 import getNewSale, getId


def addSale(id, titlu, gen, pret, tip_red_cl, lista):
    """
    Adauga o vanzare intr-o lista
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param tip_red_cl: string
    :param lista: lista de vanzari
    :return: o lista continand vechile vanzari si noua vanzare
    """
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja! ")
    sale = getNewSale(id, titlu, gen, pret, tip_red_cl)
    return lista + [sale]


def getById(id, lista):
    """
    Da vanzarea din lista cu un id dat
    :param id: string
    :param lista: lista de vanzari
    :return: vanzarea cu id-ul dat sau None daca nu exista
    """
    for sale in lista:
        if getId(sale) == id:
            return sale
    return None


def deleteSale(id, lista):
    """
    Sterge vanzarea cu id-ul dat dintr-o lista
    :param id: id-ul vanzarii care se va sterge
    :param lista: lista de vanzari
    :return: o lista de vanzari fara vanzarea cu id-ul dat
    """
    if getById(id, lista) is None:
        raise ValueError("Id-ul nu exista!")

    return [sale for sale in lista if getId(sale) != id]


def modifySale(id, titlu, gen, pret, tip_red_cl, lista):
    """
    Modifica vanzarea cu id-ul dat
    :param id: id-ul vanzarii
    :param titlu: titlul cartii
    :param gen: genul cartii
    :param pret: pretul cartii
    :param tip_red_cl: tipul de reducere al clientului
    :param lista: o lista de vanzari
    :return: lista modificata
    """
    if getById(id, lista) is None:
        raise ValueError("Id-ul nu exista! ")

    listaNoua = []
    for sale in lista:
        if getId(sale) == id:
            newSale = getNewSale(id, titlu, gen, pret, tip_red_cl)
            listaNoua.append(newSale)
        else:
            listaNoua.append(sale)
    return listaNoua
