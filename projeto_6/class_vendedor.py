from class_pessoa import Pessoa

class Vendedor(Pessoa):

    # Recebemos os parametros da função 
    def __init__(self, id_= None, nome= None, idade= None, cpf= None, senha= None):
        # Chamamos o construtor da classe pai, e passamos argumentos para ela, então 
        # temos um objeto "pai", um objeto que herda da super classe, e depois personalizamos 
        # a subclasse, com métodos e atributos próprios. 

        super().__init__(id_, nome, idade, cpf)

        self.__senha = senha  


    @property 
    def senha(self):
        return senha 


    @senha.setter 
    def senha(self):
        self.__senha = senha 



    