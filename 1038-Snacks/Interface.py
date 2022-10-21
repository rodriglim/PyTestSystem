from CopularCardapio import CopularMenu
from Pedido import Pedido


class UserInterface:
    def __init__(self, menu: CopularMenu) -> None:
        self.menu = menu

    def entradaDados(self) -> Pedido:
        result = input(
            "Digite código e a quantidade(OBS:Espaço entre os valores informado)").split()
        return Pedido(int(result[0]), int(result[1]))

    def valorTotal(self, pedido: Pedido) -> float:
        return self.menu.get_Valor(pedido)

    def interacoes(self) -> bool:
        pedido = self.entradaDados()

        if (self.menu.procurarItem(pedido) == False):
            print("Código informado inválido!")
            return False

        print(f"Valor:R$ :{self.valorTotal(pedido)}")
        return True