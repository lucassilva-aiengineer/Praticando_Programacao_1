import funcoes 

class Livro: 

    def __init__(self, nome, autor, edicao, ano, editora):

        self.__nome = nome 
        self.__autor = autor 
        self.__edicao = edicao
        self.__ano = ano 
        self.__editora = editora
        self.__status = True 
        self.__id_ = funcoes.gerar_id


# Getters 

    # Definindo a lógica de leitura 
    @property 
    def nome(self):
        return self.__nome 

    @property 
    def autor(self):
        return self.__autor 

    @property 
    def edicao(self):
        return self.__edicao 

    @property 
    def ano(self):
        return self.__ano 

    @property 
    def editora(self):
        return self.__editora

    @property 
    def status(self):
        return self.__status 

    @property 
    def id_(self):
        return self.__id_


# Setters 

    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome 

    @autor.setter 
    def autor(self, novo_autor ):
        self.__autor = novo_autor 

    @edicao.setter 
    def edicao(self, nova_edicao):
        self.__edicao = nova_edicao 

    @ano.setter 
    def ano(self, novo_ano):
        self.__ano = novo_ano 

    @editora.setter 
    def editora(self, nova_editora):
        self.__editora = nova_editora 

    @status.setter 
    def status(self, novo_status):
        self.__status = novo_status 

    @id_.setter 
    def id_(self, novo_id):
        self.__id_ = novo_id 
