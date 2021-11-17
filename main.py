from logic.CRUD import addSale
from tests.testall import runAllTests
from ui.console import runMenu


def main():
    runAllTests()
    lista_sale = []
    lista_sale = addSale("1", "Alchimistul", "Fictiune", 40, "silver", lista_sale)
    lista_sale = addSale("2", "Moara cu noroc", "Nuvela psihologica", 30, "none", lista_sale)
    runMenu(lista_sale)


main()
