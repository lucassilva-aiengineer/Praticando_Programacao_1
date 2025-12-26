# O Desafio é criar uma classe estoque e criar e após isto criar 

from faker import Faker 
import class_roupa 
import random 


class EstoqueRoupas: 

    def __init__(self, roupas= None):

        self.__roupas = [] if roupas == None else roupas 


    @property 
    def roupas(self):
        return self.__roupas


    @roupas.setter
    def roupas(self, nova_roupas):
        self.__roupas = nova_roupas

# Criando muitos objetos. 

def criando_objetos_roupas():

    faker = Faker('pt_BR')

    modelos_roupas = ["Camisa", "Blazer", "Calça", "Calça Jeans", "Gravata", "Terno Completo"]

    marcas_roupas = ["Hugo Boss", "Ermenegildo Zegna", "Brooks Brothers", 
    "Giorgio Armani", "Canali", "Ricardo Almeida", 
    "Brooksfield", "Aramis", "Vila Romana", "Crawford"]

    tamanhos = ["P", "M", "G", "GG"]

    cores = ["Amerelo", "Azul", "Verde", "Amarelo", "Branco"]

    objetos_roupas = []

    roupas_criadas, objetos_criar = 0, 100
    while roupas_criadas <= objetos_criar:

        random.shuffle(modelos_roupas)

        modelo = random.choice(modelos_roupas)

        random.shuffle(marcas_roupas)

        marca = random.choice(marcas_roupas)

        random.shuffle(tamanhos)

        tamanho = random.choice(tamanhos)

        random.shuffle(cores)

        cor = random.choice(cores)

        objeto_roupa = class_roupa.Roupa(modelo, marca, tamanho, cor)

        objetos_roupas.append(objeto_roupa)

        roupas_criadas += 1

    return objetos_roupas

roupas_a = criando_objetos_roupas()

# Criando um objeto estoque. 
estoque_1 = EstoqueRoupas(roupas= roupas_a)


for roupa in estoque_1.roupas: 

    print(f"""Modelo: {roupa.modelo}
Marca: {roupa.marca}
Cor: {roupa.cor}""")

