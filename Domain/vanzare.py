def creeaza_vanzare(id_vanzare,titlu,gen,pret,tip_client):
    """
    Creeaza o vanzare.
    :param id_vanzare: id-ul vanzarii, unic
    :param titlu: titlul cartii vandute , nenul
    :param gen: genul cartii , nenul
    :param pret: pretul fara reducere ,nenul
    :param tip_client: tipul clientului ( none/silver/gold ) , nenul
    :return: o vanzare
    """
    return [
        id_vanzare,
        titlu,
        gen,
        pret,
        tip_client,

    ]

def get_id(vanzare):
    """
    Getter pentru id-ul vanzarii
    :param vanzare: vanzare
    :return: id-ul vanzarii date ca parametru
    """
    return vanzare[0]

def get_titlu(vanzare):
    """
    Getter pentru titlul cartii
    :param vanzare:  vanzare
    :return: titlul vanzarii date ca parametru
    """
    return vanzare[1]

def get_gen(vanzare):
    """
    Getter pentru genul cartii
    :param vanzare:  vanzare
    :return: genul vanzarii date ca parametru
    """
    return vanzare[2]

def get_pret(vanzare):
    """
    Getter pentru pretul cartii
    :param vanzare:  vanzare
    :return: pretul vanzarii date ca parametru
    """
    return vanzare[3]

def get_reducere(vanzare):
    """
    Getter pentru discount-ul vanzarii
    :param vanzare:  vanzare
    :return: tipul reducerii vanzarii date ca parametru
    """
    return vanzare[4]

def get_str(vanzare):
    return f'Vanzarea cu id-ul {get_id(vanzare)} a cartii {get_titlu(vanzare)} de genul {get_gen(vanzare)} a fost realizata cu pretul de {get_pret(vanzare)} catre un client {get_reducere(vanzare)}'
