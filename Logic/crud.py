from Domain.vanzare import creeazaVanzare, getId


def adaugVanzare(id, titlu, gen, pret, reducere, lista, undoList, redoList):
    '''
    adauga o vanzare intr-o lista
    :param id: id-ul unei vanzari - string
    :param titlu: titlul unei carti - string
    :param gen: genul unei carti - string
    :param pret: pretul unei carti - float
    :param reducere: tip reducere client(none, silver sau gold) - string
    :return: o lista care contine lista veche si vanzarea adaugata
    '''
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if pret < 0:
        raise ValueError("Pretul trebuie sa fie pozitiv!")
    vanzare = creeazaVanzare(id, titlu, gen, pret, reducere)
    undoList.append(lista)
    redoList.clear()
    return lista + [vanzare]

def getById(id, lista):
    '''
    ia vanzarea cu id-ul dat dintr-o lista
    :param id: id-ul vanzarii - string
    :param lista: lista de vanzari
    :return: vanzarea cu id-ul dat sau None daca nu exista in lista
    '''
    for vanzare in lista:
        if getId(vanzare) == id:
            return vanzare
    return None

def stergVanzare(id, lista, undoList, redoList):
    '''
    sterge o vanzare dintr-o lista
    :param id: id-ul vanzarii - string
    :param lista: lista de vanzari
    :return: lista fara vanzarea cu id-ul dat
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    undoList.append(lista)
    redoList.clear()
    return [vanzare for vanzare in lista if getId(vanzare) != id]

def modifVanzare(id, titlu, gen, pret, reducere, lista, undoList, redoList):
    '''
    modifica o vanzare dintr-o lista
    :param id: id-ul unei vanzari - string
    :param titlu: titlul unei carti - string
    :param gen: genul unei carti - string
    :param pret: pretul unei carti - float
    :param reducere: tip reducere client(none, silver sau gold) - string
    :return: lista cu vanzarea modificata
    '''
    if getById(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat!")
    listaN =[]
    for vanzare in lista:
        if getId(vanzare) == id:
            vanzareNoua = creeazaVanzare(id, titlu, gen, pret, reducere)
            listaN.append(vanzareNoua)
        else:
            listaN.append(vanzare)
    undoList.append(lista)
    redoList.clear()
    return listaN


