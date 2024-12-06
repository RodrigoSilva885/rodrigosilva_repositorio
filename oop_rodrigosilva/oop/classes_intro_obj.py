#Importar as classes do ficheiro que tem as classes
from classes_intro_blueprints import Pessoa
from classes_intro_blueprints import Carro

#Instanciação da classe pessoa
pessoa = Pessoa("Rodrigo", 16)

#Instanciação da classe carro
carro = Carro("Ferrari", 812)

#Chamar a função da classe, utilizando os dados que eu atribui na instanciação
print(pessoa.saudacao())
print(carro.informacao_do_carro())