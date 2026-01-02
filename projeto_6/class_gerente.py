from class_pessoa import Pessoa 
import class_vendedor

class Gerente(Pessoa):

    def __init__(self, id_= None, nome= None, idade= None, cpf= None, senha= None, equipe= None, \
    loja= None):

        super().__init__(id_, nome, cpf, idade)

        self.__equipe = [] if not equipe else equipe 
        self.__loja = loja_atual if loja_atual else None
        self.__senha = senha

    @property 
    def equipe(self):
        return self.__equipe 


    @property 
    def loja(self):
        return self.__loja 


    @property 
    def senha(self):
        return self.__senha 


    # Defindo os setters. 
    # Os métodos de escrita. 

    @equipe.setter 
    def equipe(self, nova_equipe: list):
        """ Neste atributo temos uma lista com os objetos que são 
        subordinados ao objeto gerente """
        self.__equipe = nova_equipe 


    @loja.setter
    def loja(self, nova_loja: str):
        self.__loja = novo_loja 


    @senha.setter 
    def senha(self, nova_senha: str):
        self.__senha = nova_senha


    # Criando um método de contratação 
    def contratar(self):

        """Este método permite ao usuário contratar, adicionando, ou despedir funcionários, alterando o status 
        de contratação. """

        while True:

            print("Para contratar um novo ficionário digite 1")

            opcao = input("Indique a sua opção.")

            if opcao == "1":
                nome = input("Indique o nome do candidato: ")

                idade: int = input(f"Indique a idade do candidato {nome}")

                cpf: str = input(f"Indique o cpf do candidato {nome}: ")

                senha = funcoes.gerar_senha()

                cargo = input("Indique o")



# pessoas = None 
# if not pessoas: 
#     print(pessoas)