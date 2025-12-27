class Operador:

    """O operador é o usuário especial capaz de alterar o estoque"""

    def __init__(self, nome= None, senha= None, id_ = None):

        self.__nome = nome 
        self.__senha = senha 
        self.__id_ = id_ 


    # Getters, leitura
    @property 
    def nome(self): # O próprio objeto é passado como parâmetro e dessa forma o atributo é acessado. 
        return self.__nome 


    @property 
    def senha(self):
        return self.__senha 


    @property 
    def id_(self):
        return self.__id_ 


    #  Setters, escrita. 
    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome 


    @senha.setter 
    def senha(self, nova_senha):
        self.__senha = nova_senha 


    @id_.setter 
    def id_(self, novo_id):
        self.__id_ = novo_id
