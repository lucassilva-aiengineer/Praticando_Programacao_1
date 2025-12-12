# Criando uma classe produto, destinada ao design dos próximos produtos. 
from datetime import datetime, timedelta

class Produto:

    def __init__(self, nome, preco, custo, quantidade, validade):

        # Privando os atributos para que eles não sejam acessados de forma pública. 

        self.__nome = nome 
        self.__preco = preco 
        self.__custo = custo 
        self.__quantidade = quantidade
        self.__imposto = 0
        self.__validade = datetime.now() + timedelta(days= validade) 
        self.__data_criacao = datetime.now()

    # Definindo a regra de leitura, no caso por enquanto teremos uma regra de leitura 
    # simples bem parecida com a leitura de um atributo público. 

    # Atributos privados métodos públicos. 

    # Getters 
    @property 
    def nome(self):
        return self.__nome 

    @property 
    def preco(self):

        # Utilizamos o self para acessar os atributos do próprio objeto, bem parecido com o
        # que fazemos com objetos que já foram criados. 

        return self.__preco 

    @property 
    def custo(self):
        return self.__custo 

    @property
    def imposto(self):
        return self.__imposto 

    @property 
    def validade(self):

        senha = int(input("Digite a sua senha: "))

        if senha == 1234:
            return self.__validade 

        else:
            return "Acesso negado!"


    @property
    def data_criacao(self):
        return self.__data_criacao 


    # Setters 
    # Desenvolvendo a nossa regra ed escrita. 

    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome


    @preco.setter 
    def preco(self, novo_preco):
        self.__preco = novo_preco 


    @custo.setter 
    def custo(self, novo_custo):
        self.__custo = novo_custo 


    @imposto.setter 
    def imposto(self, novo_imposto):
        self.__imposto = novo_imposto 


    





produto_1 = Produto("Refrigerante", 10.99, 5, 10)


validade_do_produto = produto_1.validade

print(validade_do_produto) 

# print(produto_1.)


