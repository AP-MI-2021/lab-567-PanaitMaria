from Domain.vanzare import get_str, creeaza_vanzare
from Logic.crud import create, update, delete
from Logic.discount import aplicare_discount
from Logic.modificare_gen import modificare_gen
from Logic.modify_min_price_each_genre import genres_list, min_price_by_genre
from Logic.sort_ascending import sort_ascending
from Logic.titles_count_each_genre import distinct_titles
from Logic.undo_redo import do_undo, do_redo
from UserInterface.command_line_console import clc


def show_menu():
    print('1.CRUD')
    print('2.Aplicare discount')
    print('3.Modificare gen pentru un titlu dat')
    print('4.Determinare pret minim pentru fiecare gen')
    print('5.Ordonara vanzarilor crescator dupa pret')
    print('6.Afisarea numarului de titluri distincte pentru fiecare gen')
    print('a.Afisare lista vanzari')
    print('u.Undo')
    print('r.Redo')
    print('8.Command_line_console')
    print('x.Exit')


def show_crud_menu():
    print('1.Adaugare')
    print('2.Modificare')
    print('3.Stergere')
    print('a.Afisare')
    print('b.Revenire')


def handle_add(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii:'))
    except ValueError as error:
        print('ID-ul introdus nu este un numar valid!', error)
        id_vanzare = int(input('Dati id-ul vanzarii:'))
    titlu = input('Dati titlul cartii din vanzare:')
    gen = input('Dati genul cartii vandute:')
    try:
        pret = float(input('Dati pretul vanzarii:'))
    except ValueError as error:
        print('Pretul introdus nu este valid!', error)
        pret = float(input('Dati pretul vanzarii:'))
    tip_client = input('Dati tipul de client:')
    return create(vanzari, id_vanzare, titlu, gen, pret, tip_client, undo_list, redo_list)


def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_str(vanzare))


def handle_update(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii care se actualizeaza:'))
        titlu = input('Dati noul titlul al cartii din vanzare:')
        gen = input('Dati noul gen al cartii vandute:')
        pret = float(input('Dati noul pret al vanzarii:'))
        tip_client = input('Dati noul tip de client:')
        return update(vanzari, creeaza_vanzare(id_vanzare, titlu, gen, pret, tip_client), undo_list, redo_list)
    except ValueError as error:
        print('Eroare!', error)


def handle_delete(vanzari, undo_list, redo_list):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii care se va sterge:'))
        vanzari = delete(vanzari, id_vanzare, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes.')
        return vanzari
    except ValueError as error:
        print('Eroare!', error)


def handle_modif_gen(vanzari, undo_list, redo_list):
    titlu = input(f"Introduceti titlul cartii pentru care se va schimba genul:")
    new_gen = input(f"Introduceti noul gen al cartii {titlu}:")
    vanzari = modificare_gen(vanzari, titlu, new_gen, undo_list, redo_list)
    return vanzari


def handle_crud(vanzari, undo_list, redo_list):
    while True:
        show_crud_menu()
        optiune = input('Optiunea aleasa:')
        if optiune == '1':
            vanzari = handle_add(vanzari, undo_list, redo_list)
        elif optiune == '2':
            vanzari = handle_update(vanzari, undo_list, redo_list)
        elif optiune == '3':
            vanzari = handle_delete(vanzari, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(vanzari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return vanzari


def handle_console(vanzari):
    return clc(vanzari)


def handle_sort_ascending(vanzari, undo_list, redo_list):
    vanzari_aranjate = sort_ascending(vanzari, undo_list, redo_list)

    return vanzari_aranjate


def handle_min_price(vanzari):
    genuri = genres_list(vanzari)
    preturi_minime = min_price_by_genre(vanzari)
    for i in range(0, len(genuri)):
        print(f'Genul {genuri[i]} are pretul minim de {preturi_minime[i]}.')


def handle_titluri_gen(vanzari):
    nt, g = distinct_titles(vanzari)
    for i in range(0, len(nt)):
        print(f'Genul {g[i]} are {nt[i]} titluri.')


def handle_undo(vanzari, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, vanzari)
    if undo_result is not None:
        return undo_result
    return vanzari


def handle_redo(vanzari, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, vanzari)
    if redo_result is not None:
        return redo_result
    return vanzari


def run_ui(vanzari, undo_list, redo_list):
    while True:
        show_menu()
        opt = input('Optiunea aleasa:')
        if opt == '1':
            vanzari = handle_crud(vanzari, undo_list, redo_list)
        elif opt == '2':
            vanzari = aplicare_discount(vanzari, undo_list, redo_list)
        elif opt == '3':
            vanzari = handle_modif_gen(vanzari, undo_list, redo_list)
        elif opt == '4':
            handle_min_price(vanzari)
        elif opt == '5':
            vanzari = handle_sort_ascending(vanzari, undo_list, redo_list)
        elif opt == '6':
            handle_titluri_gen(vanzari)
        elif opt == '8':
            vanzari = handle_console(vanzari)
        elif opt == 'a':
            handle_show_all(vanzari)
        elif opt == 'u':
            vanzari = handle_undo(vanzari, undo_list, redo_list)
        elif opt == 'r':
            vanzari = handle_redo(vanzari, undo_list, redo_list)
        elif opt == 'x':
            break
        else:
            print('Optiune invalida.')
    return vanzari
