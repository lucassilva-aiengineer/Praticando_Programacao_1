from livraria import Livraria
from livro import Livro 
from usuario import Usuario 
from faker import Faker



# Criamos uma livraria e adicionamos a ela algumas objetos livro. 


def funcao_main():

    faker = Faker('pt_BR')

    livraria_1 = Livraria()

    for valor in range(0, 10):

        livraria_1.adicionar_livro(automatico= True, nome= nome_a, autor= editora_a, edicao= edicao_a, ano= ano_a, editora= editora_a)
        