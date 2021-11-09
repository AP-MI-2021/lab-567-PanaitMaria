from Domain.vanzare import creeaza_vanzare, get_id


def create(lst_vanzari,
           id_vanzare, titlu, gen, pret, tip_client,
           undo_list,redo_list):
    """
    Creeaza o lista de vanzari
    :param redo_list: lista redo
    :param undo_list: lista undo
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii
    :param titlu: titlul cartii vandute
    :param gen: genul cartii vandute
    :param pret: pretul cartii
    :param tip_client: tipul de client
    :return: O noua lista formata din lst_vanzari si noua vanzare adaugata
    """


    vanzare = creeaza_vanzare(id_vanzare, titlu, gen, pret, tip_client)

    undo_list.append(lst_vanzari)
    redo_list.clear()

    return lst_vanzari + [vanzare]


def read(lst_vanzari, id_vanzare=None):
    """
    Citeste o vanzare din "baza de date"
    :param lst_vanzari: lista de vanzari
    :param id_vanzare: id-ul vanzarii
    :return: vanzara cu id-ul id_vanzare sau lista cu toate vanzarile daca id_vanzare=None
    """
    vanzare_cu_id = None
    for vanzare in lst_vanzari:
        if get_id(vanzare) == id_vanzare:
            vanzare_cu_id = vanzare
    if vanzare_cu_id:
        return vanzare_cu_id
    return lst_vanzari


def update(lst_vanzari, new_vanzare,
           undo_list,redo_list):
    """
    Actualizeaza o vanzare
    :param redo_list: lista redo
    :param undo_list: lista undo
    :param lst_vanzari: lista de vanzari
    :param new_vanzare: vanzarea care se va actualiza - id-ul trebuie sa fie unul existent
    :return: o lista cu vanzarea actualizata
    """
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != get_id(new_vanzare):
            new_vanzari.append(vanzare)
        else:
            new_vanzari.append(new_vanzare)

    undo_list.append(lst_vanzari)
    redo_list.clear()

    return new_vanzari


def delete(lst_vanzari, id_vanzare,
           undo_list,redo_list):
    """
    Sterge o vanzare din lst
    :param redo_list: lista undo
    :param undo_list: lista redo
    :param lst_vanzari: lista cu toate vanzarile
    :param id_vanzare: id-ul vanzarii ce se va sterge
    :return: o lista de vanzari fara vanzara cu id-ul id_vanzare
    """
    new_vanzari = []
    for vanzare in lst_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_vanzari.append(vanzare)

    undo_list.append(lst_vanzari)
    redo_list.clear()

    return new_vanzari
