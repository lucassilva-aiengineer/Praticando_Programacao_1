from livro import Livro

class Livraria:

    def __init__(self, nome, contato):

        self.__nome = nome
        self.__contato = contato
        self.__livros = []
        self.__leitores_mes = []

    # Definindo os getters
    # A lógica de leitura que irá possíbilitar o acesso aos atributos. 

    @property 
    def nome(self):
        return self.__nome

    @property
    def contato(self):
        return self.__contato 

    @property 
    def livros(self):
        return self.__livros 

    @property 
    def leitores_mes(self):
        return self.__leitores_mes

    # Defindo uma regra de escrita. 
    # pela qual nós poderemos modificar os atributos. 

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome 

    @contato.setter 
    def contato(self, novo_contato):
        self.__contato = novo_contato 

    @livros.setter 
    def livros(self, novos_livros):
        self.__livros = novos_livros

    @leitores_mes
    def leitores_mes(self, novos_leitores_mes):
        self.__leitores_mes = novos_leitores_mes



    def adicionar_livro(self, automatico= False, \
        nome= None, autor= None, edicao= None, ano= None, editora= None):


        if automatico == False:

            livros_criar = int(input("Indique a quantidade de livros que você gostaria de criar: "))
            livros_criados = 0
            while livros_criados <= livros_criar:

                nome = input("Indique o nome do livro que você gostaria de adicionar: ")
                autor = input("Indique o nome do autor deste livro: ")
                edicao = input("Indique a edição deste livro: ")
                ano = input("Indique o ano deste livro: ")
                editora = input("Indique o nome editora deste livro: ")

                livro_a = Livro(nome, autor, edicao, ano, editora)

                self.__livros += livro_a

                livros_criados += 1


        else: 

            livro_a = Livro(nome, autor, edicao, ano, editora)
            self.__livros.append(livro_a)


        
    def exibir_livros(self): 

        for livro in self.__livros: 

            status = None 

            if livro.status == True: 
                status = "Disponível"

            else: 
                status = "Indisponível"

            print(f""" ======================

Id: {livro.id_}
Título: {livro.nome}
Autor: {livro.autor}
Edição: {livro.edicao}
Ano: {livro.ano}
Editora: {livro.editora} 
Status: {status}

======================""")

