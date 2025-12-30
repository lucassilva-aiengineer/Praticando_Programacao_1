from class_operador import OperadorComum 
from class_roupa import Roupa 
from class_estoque_roupas import EstoqueRoupas

from faker import Faker
import random 





def criando_objetos_roupas():

    faker = Faker('pt_BR')

    modelos_roupas = ["Camisa", "Blazer", "Calça", "Calça Jeans", "Gravata", "Terno Completo"]

    marcas_roupas = ["Hugo Boss", "Ermenegildo Zegna", "Brooks Brothers", 
    "Giorgio Armani", "Canali", "Ricardo Almeida", 
    "Brooksfield", "Aramis", "Vila Romana", "Crawford"]

    tamanhos = ["P", "M", "G", "GG"]

    cores = ["Amerelo", "Azul", "Verde", "Amarelo", "Branco"]

    objetos_roupas = []

    roupas_criadas, objetos_criar = 0, 100
    while roupas_criadas <= objetos_criar:

        random.shuffle(modelos_roupas)

        modelo = random.choice(modelos_roupas)

        random.shuffle(marcas_roupas)

        marca = random.choice(marcas_roupas)

        random.shuffle(tamanhos)

        tamanho = random.choice(tamanhos)

        random.shuffle(cores)

        cor = random.choice(cores)

        quantidade = random.randint(0, 100)

        objeto_roupa = Roupa(modelo, marca, tamanho, cor, quantidade)

        objetos_roupas.append(objeto_roupa)

        roupas_criadas += 1

    return objetos_roupas



# Criando uma lista de objetos roupa. 

# lista_objetos_roupa = criando_objetos_roupas()


# Criando um objeto operador. 

operador_a = OperadorComum(nome= "Mateus", senha= "abcd", id_= "mateus_1")


# Criando o objeto estoque. 

# estoque_1 = EstoqueRoupas(lista_objetos_roupa, operador_a)  

estoque_2 = EstoqueRoupas(operadores= [operador_a])


roupas_no_estoque = estoque_2.roupas 


# Terminar o teste. 



def visualizando_estoque(lista_estoque):
    for roupa in lista_estoque:

        print(f"""Nome: {roupa.modelo}
    Marca: {roupa.marca}
    Tamanho: {roupa.tamanho}
    Cor: {roupa.cor}
    Quantidade: {roupa.quantidade}""")


visualizando_estoque(roupas_no_estoque) 

# Testando as manipulações do estoque. 

estoque_2.adicionar_modelos()

roupas_no_estoque = estoque_2.roupas

visualizando_estoque(roupas_no_estoque)