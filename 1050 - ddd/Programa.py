from classeDestino import Destino
from classeDestinoRepository import DestinoRepository
from Interface import UserInterface


destino = DestinoRepository()
destino.set_adicionarDDD(Destino(61, "Brasília"))
destino.set_adicionarDDD(Destino(71, "Salvador"))
destino.set_adicionarDDD(Destino(11, "São Paulo"))
destino.set_adicionarDDD(Destino(21, "Rio de Janeiro"))
destino.set_adicionarDDD(Destino(32, "Juiz de Fora"))
destino.set_adicionarDDD(Destino(19, "Campinas"))
destino.set_adicionarDDD(Destino(27, "Vitoria"))
destino.set_adicionarDDD(Destino(31, "Belo Horizonte"))


print(destino)

user_interface = UserInterface(destino)

while user_interface.get_interacao():
    pass