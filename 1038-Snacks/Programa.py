from Cardapio import MenuItem
from CopularCardapio import CopularMenu

from Interface import UserInterface

cardapio = CopularMenu()
cardapio.set_adicionarItem(MenuItem(1, "Pizza", 4.00))
cardapio.set_adicionarItem(MenuItem(2, "Refrigerant", 1.50))

print(cardapio)

interface = UserInterface(cardapio.get_Valor)

while interface.interacoes():
    pass