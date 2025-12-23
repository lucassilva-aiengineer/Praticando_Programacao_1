import funcoes 

class Igrediente: 

    def __init__(self, nome, custo, peso, quantidade, validade, fornecedor):

        self.__id_ = funcoes.gerar_id()
        self.__nome = nome 
        self.__custo = custo
        self.__peso = peso 
        self.__quantidade = quantidade 
        self.__validade = validade 
        self.__fornecedor = fornecedor 


    # Definindo o encapsulamento 
    # Construindo uma lógica que permite o aceso controlado aos atributos dos objetos de uma forma controlada, 
    # tanto em relação a leitura, os getters (property), quanto em relação a escrita os setters. 

    @property 
    def id_(self):
        return self.__id_


    @property 
    def nome(self):
        return self.__nome 


    @property 
    def custo(self):
        return self.__custo


    @property 
    def peso(self):
        return self.__peso 


    @property 
    def quantidade(self):
        return self.__quantidade 


    @property 
    def validade(self):
        return self.__validade 


    @property 
    def fornecedor(self):
        return self.__fornecedor 


    # Desenvolvendo uma lógica que nos permite o acesso, a leitura, dos nossos atributos.
    # Getters 

    @id_.getter 
    def id_(self, novo_id):
        self.__id_ = novo_id 

    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome 


    @custo.setter 
    def custo(self, novo_custo):
        self.__custo = novo_custo 


    @peso.setter 
    def peso(self, novo_peso):
        self.__peso = novo_peso 


    @quantidade.setter 
    def quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade


    @validade.setter 
    def validade(self, nova_validade):
        self.__validade = nova_validade 


    @fornecedor.setter 
    def fornecedor(self, novo_fornecedor):
        self.__fornecedor = novo_fornecedo        






igrediente_1 = Igrediente("Muzzarela",\
                28.90, 1, 100, "10/12/2026", "Centro-oeste Alimentos")



def lista_igredientes():

    objetos = []

    for a in range(0, 10):

        # id_ = input("Indique o id deste produto: ")
        nome = input("Indique o nome do igrediente: ")
        custo = float(input("Indique o custo da unidade deste igrediente: "))
        peso = float(input("Indique o peso da unidade deste igrediente: "))
        quantidade = int(input("Indique a quantidade destes produtos: "))
        validade = input("Indique a data de válidade deste lote: ")
        fornecedor = input("Indique o nome do fornecedor: ")


        novo_objeto = Igrediente(nome, custo, peso, quantidade, validade, \
            fornecedor)


        objetos.append(novo_objeto)

    return objetos 


lista_igredientes_1 = lista_igredientes()


