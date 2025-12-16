from livraria import Livraria
from livro import Livro 
from usuario import Usuario 
from faker import Faker
import random
from funcoes import adicionar_livros
import time 



# Criamos uma livraria e adicionamos a ela algumas objetos livro. 


lista_livros = ["A história dos Estados Unidos", "A história da formação do Reino Unido", "O descobrimento do Brasil", 
    "A história de portugal", "A história do descobrimento da América", "Viagens marítmas", "Descobridores da América", 
    "A independência das colônias", "A invenção do motor a vapor", "Como a criação do telefone pode acelerar o avanço das cidades"]



def funcao_main(lista_titulos):



    livraria_1 = Livraria("Livraria Tempo Novo.", "(62) 00000-0000")

    # Criando livros e adicionando a memória. 
    adicionar_livros(lista_livros, livraria_1)

    def run(): 

        print("Bem vindo a Livraria: ", livraria_1.nome)
        while True: 

            print("Caso você queira adicionar ver o catálogo de livros digite 1.")
            time.sleep(2)
            print("Caso você queira tomar um livro emprestado digite 2.")
            time.sleep(2)

            opcao = int(input("Indique a sua opção: "))

            if opcao == 1: 

                pass 





    livraria_1.exibir_livros()


funcao_main(lista_livros)
