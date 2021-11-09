def creeazaVanzare(id, titlu, gen, pret, reducere):
    '''
    creeaza un dictionar ce retine o vanzare de carte
    :param id: id-ul unei vanzari - string
    :param titlu: titlul unei carti - string
    :param gen: genul unei carti - string
    :param pret: pretul unei carti - float
    :param reducere: tip reducere client(none, silver sau gold) - string
    :return: un dictionar ce retine o vanzare de carte
    '''
    '''
    return {
        "id": id,
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "reducere": reducere

    }
    '''
    return [id, titlu, gen, pret, reducere]

def getId(vanzare):
    '''
    da id-ul vanzarii
    :param vanzare: un dictionar de tip vanzare
    :return: id-ul vanzarii - string
    '''
    #return vanzare["id"]
    return vanzare[0]


def getTitlu(vanzare):
    '''
    da titlul cartii
    :param vanzare: un dictionar de tip vanzare
    :return: titlul cartii - string
    '''
    #return vanzare["titlu"]
    return vanzare[1]

def getGen(vanzare):
    '''
    da genul cartii
    :param vanzare: un dictionar de tip vanzare
    :return: genul cartii - string
    '''
    #return vanzare["gen"]
    return vanzare[2]

def getPret(vanzare):
    '''
    da pretul cartii
    :param vanzare: un dictionar de tip vanzare
    :return: pretul cartii - float
    '''
    #return vanzare["pret"]
    return vanzare[3]

def getReducere(vanzare):
    '''
    da tipul de reducere - none, silver sau gold
    :param vanzare: un dictionar de tip vanzare
    :return: tipul de reducere al unui client
    '''
    #return vanzare["reducere"]
    return vanzare[4]

def toString(vanzare):
    '''
    scrie dictionarul sub forma de string
    :param vanzare:un dictionar de tip vanzare
    :return: disctionarul ca string
    '''
    return "id: {}, titlu: {}, gen: {}, pret: {}, reducere: {}".format(
        getId(vanzare),
        getTitlu(vanzare),
        getGen(vanzare),
        getPret(vanzare),
        getReducere(vanzare)
    )