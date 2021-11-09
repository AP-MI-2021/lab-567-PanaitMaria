from Domain.vanzare import get_pret
from Logic.sort_ascending import sort_ascending
from Tests.test_crud import get_data


def test_sort_ascending():
    vanzari=get_data()
    vanzari_ordonate=sort_ascending(vanzari,[],[])
    pmin = get_pret(vanzari_ordonate[0])
    assert len(vanzari) == len(vanzari_ordonate)
    for vanzare in vanzari_ordonate:
        assert get_pret(vanzare) >= pmin
        pmin=get_pret(vanzare)