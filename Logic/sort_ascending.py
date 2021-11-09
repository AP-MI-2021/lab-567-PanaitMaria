from Domain.vanzare import get_pret


def ascending_prices(vanzari):
    """
    creeaza o lista ce contine preturile asezate in ordine crescatoare
    :param vanzari: lista vanzarilor
    :return: lista cu preturile asezate in ordine crescatoare
    """
    prices=[]
    for vanzare in vanzari:
        price=get_pret(vanzare)
        prices.append(price)
    prices.sort()
    return prices

def sort_ascending(vanzari,undo_list,redo_list):
    """
    Lista cu vanzarile ordonate crescator dupa pret, pastrandu-si id-ul initial
    :param vanzari: lista vanzarilor
    :return:lista vanzarilor ordonate crescator dupa pret
    """
    prices=ascending_prices(vanzari)
    vanzari_ordonate=[]
    i=0
    while i < len(prices):
        for vanzare in vanzari:
            if i<len(prices) and get_pret(vanzare) == prices[i]:
                vanzari_ordonate.append(vanzare)
                i+=1
    undo_list.append(vanzari)
    redo_list.clear()
    return vanzari_ordonate
