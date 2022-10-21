from classeDestino import Destino
from classeDestinoRepository import DestinoRepository
from classeUsuario import Usuario


def test_addProduto():
    # Arrange
    menu_repository = DestinoRepository()
    menu_repository.destino = []
    menu1 = Destino(11, "São Paulo")
    menu2 = Destino(21, "Rio de Janeiro")
    menu3 = Destino(41, "Curitiba")


    # Act

    menu_repository.set_adicionarDDD(menu1)
    menu_repository.set_adicionarDDD(menu2)



    # Assert
    assert len(menu_repository.destino_item) == 2
    assert not menu3 in menu_repository.destino_item
    assert type(menu_repository.destino_item) == list


def test_verificarExistencia():
    # Arrange
    menu_repository = DestinoRepository()
    menu_repository.destino_item = []
    menu1 = Destino(11, "São Paulo")
    ddd1 = Usuario(11)
    ddd2 = Usuario(12)
    # Act

    menu_repository.set_adicionarDDD(menu1)
    resultNOK = menu_repository.checar_destino(ddd1)
    resultOK = menu_repository.checar_destino(ddd2)

    # Assert
    assert len(menu_repository.destino_item) == 1
    assert resultOK == True
    assert resultNOK == False