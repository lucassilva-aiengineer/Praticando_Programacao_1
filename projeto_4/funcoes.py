import random 

def gerar_id():

    id_ = ""

    caracteres_gerados = 0 
    caracteres_gerar = 5
    while caracteres_gerados <= caracteres_gerar:

        numero = random.randint(0, 9)


        id_ += str(numero)

        caracteres_gerados += 1 


    return id_ 



# print(gerar_id())