import random 

def gerar_id():

    id_ = ""

    caracteres_criados, caracteres_gerar = 0, 10
    while caracteres_criados <= caracteres_gerar:

        caracter = random.randint(0, 9)
        id_ += str(caracter)

        caracteres_criados += 1

    return id_ 

print(gerar_id()) 