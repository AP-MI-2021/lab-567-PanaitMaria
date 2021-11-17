from domain.vanzari2 import getTipRedCl, getNewSale, getId, getTitlu, getGen, getPret


def reducere(lista):
    """
        Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.
        :param lista: lista de vanzari
        :return: lista in care se aplica un discount de 5% pentru toate reducerile silver și 10% pentru toate  cele gold
    """

    lista_new = []

    for sale in lista:
        if getTipRedCl(sale) == 'silver':
            newSale = getNewSale(
                getId(sale),
                getTitlu(sale),
                getGen(sale),
                getPret(sale) - 5 / 100 * getPret(sale),
                getTipRedCl(sale),
            )
            lista_new.append(newSale)

        elif getTipRedCl(sale) == 'gold':
            newSale = getNewSale(
                getId(sale),
                getTitlu(sale),
                getGen(sale),
                getPret(sale) - 10 / 100 * getPret(sale),
                getTipRedCl(sale),
            )
            lista_new.append(newSale)
        else:
            lista_new.append(sale)
    return lista_new


def modifyGen(titlu, gen, lista):
    """
    Modificarea genului unei carti cu un anumit titlu dat.
    :param lista: lista de vanzari
    :return: lista unde se modifica genul unei carti cu titlul dat
    """

    lista_new = []

    for sale in lista:
        if getTitlu(sale) == titlu:
            newSale = getNewSale(
                getId(sale),
                getTitlu(sale),
                gen,
                getPret(sale),
                getTipRedCl(sale),
            )
            lista_new.append(newSale)
        else:
            lista_new.append(sale)

    return lista_new


def minimPriceGen(lista):
    """
    Determina pretul minim pentru fiecare gen
    :param lista: lista de vanzari
    :return: un dictionar care contine cel mai mic pret pentru fiecare gen
    """
    result = {}
    for sale in lista:
        gen = getGen(sale)
        if gen in result:
            if getPret(sale) < result[gen]:
                result[gen] = getPret(sale)
        else:
            result[gen] = getPret(sale)
    return result

def orderByPrice(lista):
    """
    Orodnarea crescatoare a vanzarilor dupa pretul lor
    :param lista: lista de vanzari
    :return: vanzarile ordonate crescator dupa pret
    """
    return sorted(lista, key=lambda sale: getPret(sale))


def titlesPerGen(lista):
    """
    Afiseaza numarul de titluri distincte pentru fiecare gen
    :param lista: lista de vanzari
    :return: un dictionar care contine numarul de titluri distincte pentru fiecare gen
    """
    result = {}
    for sale in lista:
        gen = getGen(sale)

        if gen in result:
            result[gen] = result[gen] + 1
        else:
            result[gen] = 1
    return result

