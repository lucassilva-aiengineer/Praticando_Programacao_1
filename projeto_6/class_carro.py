import time
from datetime import datetime

""" Aqui esta definida a criação dos objetos carro. """

class Carro:

    """Esta classe define a construção e formato dos objetos carros, 
    com estes atributos e métodos."""

    def __init__(self, modelo, marca, ano, quilometragem, entrada_concessionaria, proxima_revisao, \
    prazo_garantia, historico_revisao= None, historico_proprietarios= None, \
    saida_concessionaria= None): 


        # Atributos dos objetos. 

        self.__modelo = modelo 
        self.__marca = marca 
        self.__ano = ano 
        self.__quilometragem = quilometragem 
        self.__proxima_revisao = proxima_revisao 
        self.__historico_revisao = historico_revisao if  historico_revisao != None else [] 
        self.__historico_proprietarios = [] if historico_proprietarios == None else historico_proprietarios 
        self.__prazo_garantia = prazo_garantia if prazo_garantia != None else 0
        self.__entrada_concessionaria = entrada_concessionaria if entrada_concessionaria != None else datetime.now()
        self.__saida_concessionaria  = saida_concessionaria 
        self.__vendido = False if self.__saida_concessionaria == None else True

    # Definindo o encapsulamento. 
    # Construindo métodos seguros de acesso, seja de leitura ou de escrita, para com os atributos. 

    # Getters, os métodos de leitura. 
    @property 
    def modelo(self):
        return self.__modelo 


    @property 
    def marca(self):
        return self.__marca 


    @property 
    def ano(self):
        return self.__ano 


    @property 
    def quilometragem(self):
        return self.__quilometragem 


    @property 
    def proxima_revisao(self):
        return self.__proxima_revisao 


    @property 
    def historico_revisao(self):
        return self.__historico_revisao


    @property 
    def historico_proprietarios(self):
        return self.__historico_proprietarios 


    @property 
    def prazo_garantia(self):
        return self.__prazo_garantia 


    @property 
    def entrada_concessionaria(self):
        return self.__entrada_consencionaria 


    @property 
    def saida_concessionaria(self):
        return self.__saida_concessionaria 


    @property 
    def vendido(self):
        return self.__vendido 


    # Setters. 
    # Os métodos voltados a escrita. 
    @modelo.setter 
    def modelo(self, novo_modelo: str):
        self.__modelo = novo_modelo 


    @marca.setter 
    def marca(self, nova_marca: str):
        self.__marca = nova_marca 


    @ano.setter
    def ano(self, novo_ano: int):
        self.__ano = novo_ano 


    @quilometragem.setter 
    def quilometragem(self, nova_quilometragem: int):
        self.__quilometragem = nova_quilometragem 


    @proxima_revisao.setter 
    def proxima_revisao(self, nova_revisao: int):
        self.__proxima_revisao = nova_revisao 


    @historico_revisao.setter 
    def historico_revisao(self, nova_revisao: list):
        self.__historico_revisao = nova_revisao 


    @historico_proprietarios.setter 
    def historico_proprietarios(self, novo_historico: list):
        self.__historico_proprietarios = novo_historico 


    @prazo_garantia.setter 
    def prazo_garantia(self, novo_prazo: int):
        self.__prazo_garantia = novo_prazo 


    @entrada_concessionaria.setter 
    def entrada_concessionaria(self, nova_entrada: str):
        self.__nova_entrada = nova_entrada 


    @saida_concessionaria.setter 
    def saida_concessionaria(self, nova_saida: str):
        self.__saida_concessionaria = nova_saida 


    @vendido.setter 
    def vendido(self):
        return self.__vendido


# Testando o objeto. 

carro_1 = Carro("Cobalt", "Chevrolet", "2018", 60000, "31-12-2025", "10-05-2027", None, None, "31-12-2025")


print(carro_1.vendido)

# print(help(Carro))
