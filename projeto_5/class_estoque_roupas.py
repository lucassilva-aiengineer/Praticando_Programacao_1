# O Desafio é criar uma classe estoque e criar e após isto criar 

from faker import Faker 
import class_roupa 
import random 
import time 
from datetime import datetime

class EstoqueRoupas: 

    def __init__(self, roupas= None, operadores= None):

        self.__roupas = [] if roupas == None else roupas 
        self.__operadores = [] if operadores == None else operadores 
        self.__historico_operacoes_true = []
        self.__historico_operacoes_false = []

    @property 
    def roupas(self):
        return self.__roupas


    @roupas.setter
    def roupas(self, nova_roupas):
        self.__roupas = nova_roupas


    # Criando os métodos dos objetos, ou métodos da classe. 

    def adicionar_modelos(self):

        tentativas_realizadas = 0
        while tentativas_realizadas <= 3:

            nome = input("Indique o seu nome: ")
            senha = input("Indique a sua senha: ")

            permitir_alteracao = False
            for operador in self.__operadores:

                # A senha deverá utilizar apenas letras minúsculas. 

                if operador.nome == nome:

                    if operador.senha == senha.lower():

                        print("Usuário encontrado...")
                        time.sleep(2)

                        relatorio = {}

                        horario = datetime.now()

                        relatorio["alterador"] = operador.nome 
                        relatorio["horario"]   = horario 
                        # relatorio["objeto"] = operador 
                        relatorio["id"] = operador.id

                        self.__historico_operacoes_true.append(relatorio)

                        print("Acesso permitido...")
                        time.sleep(2)

                        print("Prossegindo com a operação. ")
                        time.sleep(2)

                        break

                    else: 

                        print("Senha inválida...")
                        time.sleep(2)

                        print("Tentando novamente...")
                        time.sleep(2)
                        tentativas_realizadas += 1

                else: 

                    print("Nome de usuário inválido...")
                    time.sleep(2)

                    print("Tentando novamente...")
                    time.sleep(2)

                    tentativas_realizadas += 1

            relatorio_tentativa_frustrada = {}

            relatorio_tentativa_frustrada["alterador"] = nome 
            relatorio_tentativa_frustrada["horario"] = datetime.now()
            relatorio_tentativa_frustrada["senha"] = senha

            self.__historico_operacoes_false.append(relatorio_tentativa_frustrada)

        print("Infelismente você não conseguiu acessar o estoque.")
        time.sleep(2)

        print("As medidas de segurança voltadas para este tipo de situação foram tomadas.")

        time.sleep(2)




        if permitir_operacao == True:

            print("Olá!")
            time.sleep(2)
            print("Bem vindo ao estoque!")
            time.sleep(2)
            print("...")

            time.sleep(2)

            roupas_lista = []

            while True: 

                print("Para Adicionar um novo modelo ao estoque digite 1.")
                time.sleep(2)
                print("Para sair digite 2.")
                time.sleep(2)

                opcao = int(input("Indique a sua opcao: "))

                if opcao == 1:

                    modelo = input("Indique o modelo da roupas que você está adicionando ao estoque: ")
                    marca = input("Indique a marca da roupas: ")
                    tamanho = input("Indique o tamanho das roupas (M, P, G, GG): ")
                    cor = input("Indique o nome da cor das roupas:  ")
                    quantidade = int(input("Indique a quantidade deste modelo que você está adicionando: "))

                    roupa = class_roupa.Roupa(modelo, marca, tamanho, cor, quantidade)

                    roupas_lista.append(roupa)

                elif opcao == 2: 

                    print("Obrigador por trabalhar conosco.")
                    print("Saindo...")

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

        quantidade = random.randint(0, 100)

        objeto_roupa = class_roupa.Roupa(modelo, marca, tamanho, cor, quantidade)

        objetos_roupas.append(objeto_roupa)

        roupas_criadas += 1

    return objetos_roupas

roupas_a = criando_objetos_roupas()

# Criando um objeto estoque. 
estoque_1 = EstoqueRoupas(roupas= roupas_a)


# Vou Armazenar uma quantidade de roupas em um dicionário. 

# roupas_estoque = {}

# for roupa in roupas_a: 

#     quantidade = random.randint(2, 100)

#     roupas_estoque["modelo"] = roupa 


# for roupa in estoque_1.roupas: 

#     print(f"""Modelo: {roupa.modelo}
# Marca: {roupa.marca}
# Cor: {roupa.cor}""")


