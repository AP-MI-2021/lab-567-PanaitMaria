from Logic.modify_min_price_each_genre import genres_list
from Logic.titles_count_each_genre import distinct_titles
from Tests.test_crud import get_data


def test_titles_count_each_genre():
    vanzari=get_data()
    nt,g= distinct_titles(vanzari)
    assert nt[0] == 1
    assert g[0] == 'Basm'
    assert nt[1] == 1
    assert g[1] == 'Nuvela'
    assert nt[2] == 3
    assert g[2] == 'Roman'