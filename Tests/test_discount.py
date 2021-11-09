from Domain.vanzare import get_pret, creeaza_vanzare, get_reducere
from Logic.discount import aplicare_discount


def get_data():
    return [
        creeaza_vanzare(1, 'Harap Alb', 'Basm', 10, 'gold'),
        creeaza_vanzare(2, 'Moara cu noroc', 'Nuvela', 25, 'none'),
        creeaza_vanzare(3, 'Mara', 'Roman', 30, 'gold'),
        creeaza_vanzare(4, 'Enigma Otiliei', 'Roman', 50, 'silver'),
        creeaza_vanzare(5, 'Baltagul', 'Roman', 5, 'gold'),
    ]

def test_discount():
    vanzari=get_data()
    new_vanzari=aplicare_discount(vanzari,[],[])
    for i in range (0,len(vanzari)):
        if get_reducere(vanzari[i]) != 'none':
            assert get_pret(vanzari[i]) != get_pret(new_vanzari[i])

