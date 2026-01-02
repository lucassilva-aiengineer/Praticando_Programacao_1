class Pessoa: 

    """ A classe pessoa é a classe padrão que será a base 
    de todos os objetos usuários, a classe Vendedor, Gerente e Cliente 
    irão herdar a classe pessoa, seus métodos e atributos. """

    def __init__(self, id_= None, nome= None, cpf= None, idade= None):

        self.__id_:str = id_ 
        self.__nome: str = nome if nome else ""
        self.__cpf: str = cpf if cpf else "" 
        self.__idade: int = idade if idade else 0


    # Defindo o encapsulamento. 
    # Métodos de acesso aos atributos, tanto de leitura quanto de escrita. 

    # Getters 
    # Regra de leitura.
    @property
    def id_(self):
        return self.__id_

    @property
    def nome(self):
        return self.__nome 

    @property
    def cpf(self):
        return self.__cpf

    @property
    def idade(self):
        return self.__idade 


    # Setters 
    # Defindo regras de escrita. 

    @id_.setter 
    def id_(self, novo_id):
        self.__id_ = novo_id 


    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome 


    @cpf.setter 
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf 


    @idade.setter 
    def idade(self, nova_idade):
        self.__idade = nova_idade 




# nome = None 
# if nome: 
#     print("Nome: ", nome)

# else: 
#     print("Nome: ", nome)