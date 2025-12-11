from datetime import datetime
import time
# A classe é como a arquitura, a planta baixa da casa, que cada um dos nossos objetos que serão criados 
# irão seguir, ele possuirão cada um deles um loca que será preenchido com informações próprias previamente 
# específicadas na classe, chamados atributos, também cada objeto possuirá métodos próprios que manimulam 
# os atributos ou informações internas, manipulam as informações daquele objeto singular. 

class Estoque:

    # Método dunder (double underscore) que é chamado quando o nome da classe é declarado, no caso Estoque, 
    # e este método cria espaços na memória para armazenar os objetos e seus atributos, e pode receber argumentos 
    # que podem ser atribuídos aos atributos dos objetos. 

    def __init__(self, tipo= None):

        # Privando os atributos para definirmos a lógica de encapsulamento. 

        # Este atributo armazenará objetos produto. 
        self.__produtos = []

        # Quando cada estoque for criado nós teremos o registro de tempo. 

        self.__data_criacao = datetime.now()

        self.__tipo = tipo

    # Encapsulamento

    # Getters, a lógica de leitura. 
    @property 
    def produtos(self):

        # Definindo uma lógica de leitura.
        return self.__produtos

    @property 
    def data_criacao(self):
        return self.__data_criacao

    @property 
    def tipo(self):
        return self.__tipo 

    

    def adicionar_produto(self, nome= None):

        # nome = input("Indique ") 

        if not nome: 

            def adicionado_produtos():

                quantidade_adicionar = int(input("Indique a quantidade de produtos que você gostaria de adicionar: "))

                produtos_adicionados = 0 
                while produtos_adicionados < quantidade_adicionar: 
                    nome = input("Indique o nome do produto: ")

                    # Futuramente irei criar uma classe produtos, 
                    # por enquanto estou apenas testando. 

                    produto = nome

                    self.__produtos.append(produto)

                    time.sleep(1)
                    print("Produto adicionado com sucesso!")

                    # produtos_adicionados = produtos_adicionados + 1 

                    produtos_adicionados += 1

            try: 

                adicionado_produtos()

            except TypeError as msg: 
                print(msg)
                print("A quantidade de produtos a adicionar deve ser indicada \n utilizando um tipo inteiro de dados!")
                time.sleep(2)
                print("...")
                time.sleep(2)
                print("Tentando novamente!")

                adicionado_produtos()


estoque_1 = Estoque("Calçados")

print("Tipo do Estoque:", estoque_1.tipo)
print("Produtos:", estoque_1.produtos)
print("Data de Criação do Estoque:", estoque_1.data_criacao) 

estoque_1.adicionar_produto()

# print("Produtos: " + str(estoque_1.produtos))

lista_produtos = estoque_1.produtos

print("Produtos Criados: ")
for produto in lista_produtos: 
    print(produto)


# # tempo_agora = datetime.timestamp(1)
# tempo = datetime.now()

# # print("Tempo agora: ", tempo_agora)
# print("Tempo: ", tempo)
