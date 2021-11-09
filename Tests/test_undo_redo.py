from Domain.vanzare import get_str
from Logic.crud import create
from Logic.undo_redo import do_undo, do_redo
from UserInterface.command_line_console import handle_show_all


def test_undo_redo():
    #1.Listele goale:
    list=[]
    undo_list=[]
    redo_list=[]
    list = create(list, '1', 'Baltagul', 'roman', 15, 'none', undo_list,redo_list)
    list = create(list, '2', 'Mara', 'roman', 25, 'gold', undo_list,redo_list)
    list = create(list, '3', 'Harap Alb', 'basm', 5, 'silver', undo_list,redo_list)
    print(list)
    assert len(list) == 3
    list=do_undo(undo_list,redo_list,list)
    print(list)
    assert len(list) == 2
    list = do_undo(undo_list, redo_list, list)
    print(list)
    assert len(list) == 1
    list = do_undo(undo_list, redo_list, list)
    print(list)
    assert len(list) == 0
    list = do_undo(undo_list, redo_list, list)
    assert list == None
    list=[]
    print(list)
    list = create(list, '1', 'Baltagul', 'roman', 15, 'none', undo_list, redo_list)
    list = create(list, '2', 'Mara', 'roman', 25, 'gold', undo_list, redo_list)
    list = create(list, '3', 'Harap Alb', 'basm', 5, 'silver', undo_list, redo_list)
    print(list)
    list = do_redo(undo_list,redo_list,list)
    
def main():
    test_undo_redo()


if __name__ == '__main__':
    main()