from Domain.vanzare import get_str
from Logic.crud import create, delete
def print_menu():
    print('Instructiunile sunt separate prin: [;] iar termenii prin: [,]')
    print("Pentru a adauga o vanzare scrie: 'add','id','titlu','gen','pret','reducere'.")
    print("Pentru a sterge o vanzare scrie: 'del','id'")
    print("Pentru a afisa toate vanzarile scrie: 'sa'")
    print("Pentru a inchide programul scrie: 'x'")
def handle_add(vanzari,option):
    try:
        if len(option) == 6:
            id=int(option[1])
            titlu=option[2]
            gen=option[3]
            pret=int(option[4])
            reducere=option[5]
            return create(vanzari,id,titlu,gen,pret,reducere)
        else:
            print("Eroare!")
    except ValueError as eroare:
        print('Eroare',eroare)
def handle_delete(vanzari,option):
    try:
        if len(option) == 2:
            id=int(option[1])
            vanzari=delete(vanzari,id)
            return vanzari
        else:
            print("Eroare!")
    except ValueError as eroare:
        print('Eroare ',eroare)
def handle_show_all(vanzari,option):
    for vanzare in vanzari:
        print(get_str(vanzare))
def clc(vanzari):

        while True:
            print_menu()
            lista=input()
            comenzi=lista.split(';')
            for comanda in comenzi:
                param=comanda.split(',')
                if param[0] == 'sa':
                    handle_show_all(vanzari,comanda)
                elif param[0] == 'del':
                    vanzari = handle_delete(vanzari,param)
                elif param[0] == 'x':
                    return 0,print("Program inchis")
                elif param[0] == 'add':
                    vanzari = handle_add(vanzari,param)
                else:
                    print("Optiune invalida.")