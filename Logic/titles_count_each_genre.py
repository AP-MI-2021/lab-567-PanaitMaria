from Domain.vanzare import get_gen
from Logic.modify_min_price_each_genre import genres_list
from Tests.test_crud import get_data


def distinct_titles(vanzari):
    """
    Returneaza numarul de titluri pentru fiecare gen din vanzari
    :param vanzari: lista cu vanzari
    :return: nt: lista cu numarul de titluri pentru fiecare gen
              g: lista de genuri distincte
    """
    genuri=genres_list(vanzari)
    nt=[]
    g=[]
    for gen in genuri:
        n=0
        for vanzare in vanzari:
            if gen == get_gen(vanzare):
                n+=1

        nt.append(n)
        g.append(gen)
    return nt,g
