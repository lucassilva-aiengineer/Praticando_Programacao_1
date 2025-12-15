
from datetime import datetime
""" Esta modela o objeto usuário """

class Usuario:

    def __init__(self, nome, idade, telefone, cpf, endereco):

        self.__nome = nome 
        self.__idade = idade 
        self.__telefone = telefone 
        self.__cpf = cpf 
        self.__endereco = endereco 
        self.__pontuacao = 0 
        self.__status = True 
        self.__livros__nao_devolvidos = []
        self.__livros__devolvidos = [] 
        self.__livros_danficados = [] 
        self.__criacao = datetime.now()


    