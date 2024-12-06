#Importar as classes do ficheiro que tem as classes
from classe_sobre_futebol import Vestimenta
from classe_sobre_futebol import PlayerInfo
from classe_sobre_futebol import Estatisticas

#Instanciação das classes
Vestimenta = Vestimenta("L", 46)
PlayerInfo = PlayerInfo("Águia Desnutridas", "extremo")
Estatisticas = Estatisticas(20, 13)

#Chamar a função da classe, utilizando os dados que eu atribui na instanciação
print(Vestimenta.tamanho())
print(PlayerInfo.info())
print(Estatisticas.numero_de_golos_e_assistencias())