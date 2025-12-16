import random 

def gerar_id():

    id_ = ""

    caracteres_criados, caracteres_gerar = 0, 10
    while caracteres_criados <= caracteres_gerar:

        caracter = random.randint(0, 9)
        id_ += str(caracter)

        caracteres_criados += 1

    return id_ 



# Uma funcao que cria livros automaticamente. 

def adicionar_livros(lista_titulos, livraria_a):

    faker = Faker('pt_BR')

    for valor in range(0, 10):

        random.shuffle(lista_titulos)
        titulo = random.choice(lista_titulos)
        autor_a = faker.name_male()
        edicao_a = random.randint(1, 5)
        ano_a = random.randint(1850, 2025)
        editora_a = faker.company()

        livraria_a.adicionar_livro(automatico= True, nome= titulo, autor= autor_a, edicao= edicao_a, ano= ano_a, editora= editora_a)
