from classeDestino import Destino
from classeUsuario import Usuario

class DestinoRepository:
    destino_item : Destino = []
    existeDDD = False

    def __init__(self) -> None:
        pass

    def set_adicionarDDD(self, destino : Destino) -> None:
        self.destino_item.append(destino)

    def checar_destino(self, usuario : Usuario) -> bool:
        for p in self.destino_item:
            if usuario in self.destino_item:
                DestinoRepository.existeDDD = True
            else: 
                DestinoRepository.existeDDD = False
        return DestinoRepository.existeDDD

    def obter_destino(self, DDD : Usuario) -> bool:
        if(DestinoRepository.existeDDD == True):
            return self.destino.cidade          