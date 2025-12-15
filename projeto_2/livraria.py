from livro import Livro

class Livraria:

    def __init__(self):

        self.__livros = []
        self.__contato = "(62) 99215-8128"
        self.__leitores_mes = []


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


        
        def exibir_livros(): 

            for livro in self.__livros: 

                status = None 

                if livro.status == True: 
                    status = "Disponível"

                else: 
                    status = "Indisponível"

                print(f""" ======================

Id: {livro.id}
Título: {livro.nome}
Autor: {livro.autor}
Edição: {livro.edicao}
Ano: {livro.ano}
Editora: {livro.editora} 
Status: {status}

======================""")

