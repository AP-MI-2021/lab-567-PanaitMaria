from Tests.test_crud import get_data
from UserInterface.command_line_console import print_menu, clc


def run_ui2():
    vanzari=get_data()
    vanzari=clc(vanzari)

