from Domain.vanzare import get_titlu, get_id, get_pret, get_reducere, creeaza_vanzare
from Logic.crud import update

def modificare_gen(lst_vanzari,titlu,new_gen,
                   undo_list,redo_list):
    """
    Modifica genul unei carti cu titlul dat
    :param redo_list: lista redo
    :param undo_list: lista undo
    :param lst_vanzari: lista vanzarilor
    :param titlu: titlul cartii pentru care se va schimba genul
    :return: lista cu genul modificat
    """
    undo_list.append(lst_vanzari)
    redo_list.clear()
    for vanzare in lst_vanzari:
        if get_titlu(vanzare) == titlu:
            id=get_id(vanzare)
            pret=get_pret(vanzare)
            reducere= get_reducere(vanzare)
            lst_vanzari=update(lst_vanzari,creeaza_vanzare(id,titlu,new_gen,pret,reducere),[],[])

    return lst_vanzari

