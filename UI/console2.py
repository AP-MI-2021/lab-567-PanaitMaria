from domain.vanzari2 import toString
from logic.CRUD import addSale, modifySale, deleteSale
from logic.functionality import reducere, modifyGen


def showAll(lista_sale):
    for sale in lista_sale:
        print(toString(sale))

def show_menu():
    print("""
    add: id_vanzare, titlu, gen, pret, tip_reducere_client
    delete: id_vanzare
    update: id_vanzare, titlu, gen, pret, tip_reducere_client
    gen update: titlu, gen
    reduce
    show all
    exit
     """)

def console_2(lista_sale):
    do = True
    try:
        while do:
            show_menu()
            commands = input("Introduceti comenzile separate prin ';' si instructiunile comenzii separate prin ',' ")
            command = commands.split(";")
            for i in range(len(command)):
                list_command_details = command[i].split(",")
                if list_command_details[0] == "add":
                    if len(list_command_details) != 6:
                        raise ValueError("Trebuie sa introduceti exact 5 date!")
                    id = list_command_details[1]
                    titlu = list_command_details[2]
                    gen = list_command_details[3]
                    pret = float(list_command_details[4])
                    tip_red_cl = list_command_details[5]
                    lista_sale = addSale(id, titlu, gen, pret, tip_red_cl, lista_sale)
                    print("A fost adaugata o vanzare")
                elif list_command_details[0] == "delete":
                    id = list_command_details[1]
                    lista_sale = deleteSale(id, lista_sale)
                    print("A fost stearsa o vanzare")
                elif list_command_details[0] == "update":
                    if len(list_command_details) != 6:
                        raise ValueError("Trebuie sa introduceti exact 5 date!")
                    id = list_command_details[1]
                    titlu = list_command_details[2]
                    gen = list_command_details[3]
                    pret = float(list_command_details[4])
                    tip_red_cl = list_command_details[5]
                    lista_sale = modifySale(id, titlu, gen, pret, tip_red_cl, lista_sale)
                    print("A fost modificata o vanzare")
                elif list_command_details[0] == "gen update":
                    titlu = list_command_details[1]
                    gen = list_command_details[2]
                    lista_sale = modifyGen(titlu, gen, lista_sale)
                    print("A fost schimbat genul cartii cu titlul mentionat")
                elif list_command_details[0] == "reduce":
                    lista_sale = reducere(lista_sale)
                    print("A fost aplicata reducerea")
                elif list_command_details[0] == "show all":
                    showAll(lista_sale)
                elif list_command_details[0] == "exit":
                    do = False
                else:
                    print("Comanda nu este valida! Reincercati! ")
    except Exception as ex:
        print("Eroare, reincercati!", ex)
