from Domain.vanzare import get_titlu, creeaza_vanzare, get_gen
from Logic.modificare_gen import modificare_gen


def get_data():
    return [
        creeaza_vanzare(1, 'Harap Alb', 'Basm', 10, 'gold'),
        creeaza_vanzare(2, 'Moara cu noroc', 'Nuvela', 25, 'none'),
        creeaza_vanzare(3, 'Mara', 'Roman', 30, 'gold'),
        creeaza_vanzare(4, 'Enigma Otiliei', 'Roman', 50, 'silver'),
        creeaza_vanzare(5, 'Baltagul', 'Roman', 5, 'gold'),
    ]


def test_modificare_gen():
    vanzari = get_data()
    new_vanzari = modificare_gen(vanzari, 'Moara cu noroc', 'modificat',[],[])
    for i in range(0, len(vanzari)):
        if get_titlu(vanzari[i]) == 'Moara cu noroc':
            assert get_gen(vanzari[i]) != get_gen(new_vanzari[i])
