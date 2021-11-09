from Domain.vanzare import get_gen, get_pret


def genres_list(vanzari):
    """
    Returneaza o lista ce contine genurile din vanzari
    :param vanzari: lista cu vanzari
    :return: lista cu genuri distincte
    """
    genres=[]
    for vanzare in vanzari:
        gen=get_gen(vanzare)
        if gen not in genres:
            genres.append(gen)
    return genres

def min_price_by_genre(vanzari):
    """
    Returneaza o lista ce contine preturile minime pentru fiecare gen
    :param vanzari: lista cu vanzari
    :return: lista cu preturile genurilor in ordinea in care se gasesc in vanzari
    """
    genres=genres_list(vanzari)
    preturi_minime=[]
    for gen in genres:
        pret_minim=9999999
        for vanzare in vanzari:
            if gen == get_gen(vanzare):
                pret=get_pret(vanzare)
                if pret <pret_minim:
                    pret_minim=pret
        preturi_minime.append(pret_minim)
    return preturi_minime

def handle_min_price_each_genre(vanzari):
    genres = genres_list(vanzari)
    min_prices = min_price_by_genre(vanzari)
    for i in range(0,len(genres)):
        print(f'Vanzarea cu pretul cel mai mic din genul {genres[i]} are valoarea de {min_prices[i]} lei')
