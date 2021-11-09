from Logic.crud import create
from Tests.test_crud import  test_crud
from Tests.test_discount import test_discount
from Tests.test_modificare_gen import test_modificare_gen
from Tests.test_modify_min_price_each_genre import test_modify_min_price_each_genre
from Tests.test_sort_ascending import test_sort_ascending
from Tests.test_titles_count_each_genre import test_titles_count_each_genre
from UserInterface.console import run_ui

def main():
    vanzari=[]
    undo_list=[]
    redo_list=[]
    vanzari=create(vanzari,1, 'Harap Alb', 'Basm', 15, 'gold',undo_list,redo_list)
    vanzari=create(vanzari,2, 'Moara cu noroc', 'Nuvela', 25, 'none',undo_list,redo_list)
    vanzari=create(vanzari,3, 'Mara', 'Roman', 35, 'gold',undo_list,redo_list)
    vanzari=create(vanzari,4, 'Enigma Otiliei', 'Roman', 12, 'silver',undo_list,redo_list)
    vanzari=create(vanzari,5, 'Baltagul', 'Roman', 5, 'none',undo_list,redo_list)
    vanzari=run_ui(vanzari,undo_list,redo_list)

if __name__ == '__main__':
    test_crud()
    test_discount()
    test_modificare_gen()
    test_modify_min_price_each_genre()
    test_sort_ascending()
    test_titles_count_each_genre()
    main()