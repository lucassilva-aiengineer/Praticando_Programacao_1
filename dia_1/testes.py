# import usuario
from usuario import Usuario 
from faker import Faker
import random 
import string 



# Criando uma função que apartir do nome do usuário gera um user name. 

def gerar_nome_usuario(nome):

    final = ""

    alfabeto = []
    alfabeto += string.ascii_lowercase + string.ascii_uppercase

    caracteres_especiais = ['@', '#', '-', '_', '&', '&']


    for numero in range(0, 3):

        
        numero_aleatorio = random.randint(0, 3)

        if numero_aleatorio == 0:

            random.shuffle(alfabeto)

            final += random.choice(alfabeto)

        elif numero_aleatorio == 1:

            random.shuffle(caracteres_especiais)

            final += random.choice(caracteres_especiais)

        else: 

            numero_a = random.randint(0, 9)
            final += str(numero_a) 

    user_name = nome + final

    return user_name 


# Gerador de senhas aleatório. 

def gerador_de_senhas(quantidade= 4):

    senha = ""

    caracteres_gerados = 0
    while caracteres_gerados < quantidade:

        numero_b = random.randint(0, 9)

        senha += str(numero_b)

        caracteres_gerados = caracteres_gerados + 1

        # caracteres_gerados += 1

    return senha

# Criando uma lista com 10 usuários aleatórios. 

def gerar_usuarios(quantidade):

    faker = Faker('pt_BR')

    lista_usuarios = []

    usuarios_criados, usuarios_criar = 0, quantidade 
    while usuarios_criados < usuarios_criar:

        status_a = None 

        if random.randint(0, 2) == 0:

            status_a = False 

        else:

            status_a = True 


        nome_f = faker.name_male() 

        nome_user_f, senha_f = gerar_nome_usuario(nome_f), \
        gerador_de_senhas()


        usuario_a = Usuario(nome= nome_f, nome_user= nome_user_f, senha= senha_f, status= status_a)

        lista_usuarios.append(usuario_a)

        usuarios_criados += 1

    return lista_usuarios

# faker = Faker('pt_BR')

# print(faker.user_name())

# letras = []

# letras += string.ascii_lowercase + string.ascii_uppercase

# print(letras)

# letras_2 = [string.ascii_lowercase]

# print(letras_2)


# print(gerar_usuarios())

lista_de_usuarios = gerar_usuarios(100)

letra_d = 0

for usuario in lista_de_usuarios:

    usuario_nome = usuario.nome
    if usuario_nome[0] == 'D':

        letra_d += 1


    print(usuario.nome)

print("A quantidade de nomes que iniciam com a letra D é: ", letra_d)
