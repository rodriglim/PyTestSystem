from curses.ascii import US
from classeDestinoRepository import DestinoRepository
from classeUsuario import Usuario


class UserInterface:
    def __init__(self, destino: DestinoRepository) -> None:
        self.destino = destino

    def solicitar_input(self) -> Usuario:
        result = input(
            "Informe o DDD: ").split()
        return Usuario(int(result[0]))
    
    
    def exibir_destino(self, destino: Usuario) -> int:
        return self.destino.obter_destino(destino)


    def get_interacao(self) -> bool:
        Usuario = self.solicitar_input()
        if(self.destino.checar_destino(Usuario) == False):
            print("DDD não cadastrado!")
            return False

        print(f"Cidade do DDD: {self.destino.obter_destino(Usuario)}")

        return True
