# Construindo funções que limpam strings. 



# 1) Uma função que verifica se um nome está nos padrões corretos. 


def contando_palavras(texto):

    dicionario_palavras = {}

    lista_palavras = texto.split(" ")

    for palavra in lista_palavras:

        if palavra == "":
            lista_palavras.remove(palavra)

    for palavra in lista_palavras: 

        # if palavra.startswith(letra)
        letra = palavra[0]
        if not letra in dicionario_palavras: 
            dicionario_palavras[letra] = []

        dicionario_palavras[letra].append(palavra)


    # print(palavras) 

    return dicionario_palavras

# O split(), separa uma string em uma lista de palavras apartir de 
# um separador específicado. 

texto = "Ele faz aninversário amanhã."
novo_texto = texto.split(" ")
print(novo_texto)


def main(texto_a):

    palavras_dict = contando_palavras(texto_a)

    for letra in palavras_dict: 

        print("Palavras com a letra:" + " " + letra)
        for palavra in palavras_dict[letra]:

            print(palavra)



texto_2 = """
        Era uma manhã de sábado ensolarada quando o pequeno Leo acordou com uma ideia brilhante.
        Ele correu para a cozinha, onde o cheirinho de café fresco já preenchia o ar. Lá estavam 
        seu pai, cuidando das torradas, e sua mãe, organizando as frutas da semana.
    """

print(texto_2.split(" "))

lista = texto_2.split(" ")

for palavra in lista:

    if palavra == "":
        lista.remove(palavra)

    elif palavra == "\n":
        lista.remove(palavra)

print(lista)

# print("Texto 1: ")

# print()
# # main(texto)
# print()

# print("Texto 2:")

# main(texto_2)

