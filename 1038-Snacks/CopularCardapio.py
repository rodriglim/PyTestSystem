from Cardapio import MenuItem
from Pedido import Pedido

class CopularMenu:
    itemExiste = False
    menu_item: MenuItem = []


    def __str__informacoes(self) -> str:
        formatText = "{0:<10} {1:<20} {2:<20}\n"
        menu = formatText.format("Código", "Nome", "Preço")
        for i in self.menu_itens:
            menu += formatText.format(i.id, i.name, f"$ {i.preco}")

        return menu

    def __init__(self) -> None:
        pass

    
    def set_adicionarItem(self, cardapio : MenuItem):
        self.menu_item.append(cardapio)
        
    def procurarItem(self, pedido : Pedido) -> bool:
        for p in self.menu_item:
            if pedido in self.menu_item: 
                CopularMenu.itemExiste = True
            else:
                CopularMenu.itemExiste = False
        return CopularMenu.itemExiste
    def get_Valor(self, pedido: Pedido):
        if(CopularMenu.itemExiste == True):
              return CopularMenu.set_adicionarItem * pedido.qtdProduto