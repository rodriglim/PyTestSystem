from Cardapio import MenuItem
from CopularCardapio import CopularMenu


def test_addProduto():

    menu = CopularMenu()
    menu.menu_itens = []
    menu1 = MenuItem(1, "Test 1", 10)
    menu2 = MenuItem(2, "Test 2", 5)
    menu3 = MenuItem(3, "Test 3", 2)
  

    menu.set_adicionarItem(menu1)
    menu.set_adicionarItem(menu2)


    assert len(menu.menu_item) == 2
    assert not menu3 in menu.menu_item
    assert type(menu.menu_item) == list


def test_verificarExistencia():

    menu = CopularMenu()
    menu.menu_item = []
    menu1 = MenuItem(1, "Test 1", 10)


    menu.set_adicionarItem(menu1)
    resultOK = menu.procurarItem(1)
    resultNOK = menu.procurarItem(5)

    assert len(menu.menu_item) == 1
    assert resultOK == False
    assert resultNOK == False