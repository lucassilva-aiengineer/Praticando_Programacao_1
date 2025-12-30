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

    # Definindo o encapsulamentos, essas regras de acesso, que limitam o acesso 
    # externo aos atributos, tanto em relação a leitura, os getters (@property), 
    # quanto em relação a leitura os setters. 

    # @ Getters 
    # Definindo os métodos destinados a leitura. 
    @property 
    def roupas(self):
        return self.__roupas

    @property 
    def operadores(self):
        return self.__operadores

    @property 
    def historico_operacoes_true(self):
        return self.__historico_operacoes_true 

    @property 
    def historico_operacoes_false(self):
        return self.__historico_operacoes_false


    # @Setters. 
    # Definindo os métodos orientados a escrita. 

    @roupas.setter 
    def roupas(self, novas_roupas): 
        self.__roupas = novas_roupas 


    @operadores.setter 
    def operadores(self, novos_operadores):
        self.__operadores = novos_operadores 


    @historico_operacoes_true.setter 
    def historico_operacoes_true(self, operacoes_true):
        self.__historico_operacoes_true = operacoes_true 


    @historico_operacoes_false.setter 
    def historico_operacoes_false(self, operacoes_false):
        self.__historico_operacoes_false = operacoes_false 


    # Criando os métodos dos objetos, ou métodos da classe. 

    def adicionar_modelos(self):

        permitir_alteracao = False

        tentativas_realizadas = 0
        while tentativas_realizadas <= 3:

            print("Verificação de usuário...")
            time.sleep(2)

            nome = input("Indique o seu nome: ")
            senha = input("Indique a sua senha: ")


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
                        relatorio["id"] = operador.id_

                        self.__historico_operacoes_true.append(relatorio)

                        print("Acesso permitido...")
                        time.sleep(2)

                        print("Prossegindo com a operação. ")
                        time.sleep(2)

                        permitir_alteracao = True

                        tentativas_realizadas += 4

                        # A palavra chave break serve tanto 
                        # loops for como para loops while. 

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




        if permitir_alteracao == True:

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
                    time.sleep(2)
                    print("Saindo...")

                    time.sleep(2)

                    break 


# Criando um objeto estoque. 


# Vou Armazenar uma quantidade de roupas em um dicionário. 

# roupas_estoque = {}

# for roupa in roupas_a: 

#     quantidade = random.randint(2, 100)

#     roupas_estoque["modelo"] = roupa 


# for roupa in estoque_1.roupas: 

#     print(f"""Modelo: {roupa.modelo}
# Marca: {roupa.marca}
# Cor: {roupa.cor}""")


