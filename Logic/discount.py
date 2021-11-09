from Domain.vanzare import get_id, get_titlu, get_gen, get_reducere, creeaza_vanzare, get_pret
from Logic.crud import update

def discount_silver(price):
    """
    Retruneaza pretul dupa o reducere de 5%
    :param price: pretul initial
    :return: pretul modificat
    """
    discount = price - (price*0.05)
    return discount

def discount_gold(price):
    """
    Returneaza pretul dupa o reducere de 10%
    :param price:  pretul initial
    :return: pretul modificat
    """
    discount = price - (price*0.10)
    return discount

def aplicare_discount(lst_vanzari,
                      undo_list,redo_list):
    """
    Modifica pretul vanzarilor dupa tipul de client
    :param redo_list: lista undo
    :param undo_list: lista redo
    :param lst_vanzari: lista vanzarilor
    :return: lista vanzarilor cu preturile actualizate dupa aplicarea reducerii
    """
    undo_list.append(lst_vanzari)
    redo_list.clear()

    for vanzare in lst_vanzari:
        id=get_id(vanzare)
        titlu=get_titlu(vanzare)
        gen=get_gen(vanzare)
        pret=get_pret(vanzare)
        reducere=get_reducere(vanzare)

        if reducere == 'silver':
            lst_vanzari = update(lst_vanzari,creeaza_vanzare(id,titlu,gen,discount_silver(pret),reducere),[],[])
        if reducere == 'gold':
            lst_vanzari = update(lst_vanzari, creeaza_vanzare(id, titlu, gen, discount_gold(pret), reducere),[],[])

    return lst_vanzari