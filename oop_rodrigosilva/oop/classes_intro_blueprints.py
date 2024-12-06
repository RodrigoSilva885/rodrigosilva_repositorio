#Criação de uma classe "Pessoa"
class Pessoa:

    #Função para inicializar a classe, declara a variavel nome e idade 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
       
    #Função para fazer o output da classe pessoa
    def saudacao(self):
        return f"O meu nome é {self.nome} e tenho {self.idade} anos."
 
#Criação de uma Classe "Carro" 
class Carro:

    #Função para inicializar a classe, declara a variavel marca e modelo
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    #Função para fazer o output da classe Carro
    def informacao_do_carro(self):
        return f"Este é um {self.marca} {self.modelo}."