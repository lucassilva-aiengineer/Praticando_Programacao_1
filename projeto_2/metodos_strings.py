

nome = "Lucas"

print(nome.upper())
print("Lucas".upper())

print(nome.lower())

print("mAteuS sILvA".title())
# Organiza as palavras, para que a primeira letra de cada palavra seja maiúscula enquanto as outras minúsculas. 

print("MATeus".islower()) # Verifica se todas as letras das strings são minúsculas. 

print("mAtEUS".isupper())

print("Lucas".startswith('L'))

print("Lucas".endswith('s'))

print("Lucas gosta de programar em c".replace("programar em c", "programar em c e em python e em html e em dart e em outras linguagens."))
# Substitui uma parte da string por outra parte. 

texto = "Um, dia, dois, dias, três, dias"
lista_palavras = texto.split(',')
print(lista_palavras)
# O split quebra, ou melhor, separa uma string em uma lista de palavras seguindo um separador específicado. 

# print("t e x t o".strip(" "))


# O strip() limpa as estremidades das palavras, removendo espaços ou caracteres das estremidades. 
texto_1 = "email@gmail.com   "
novo_texto = texto_1.strip()
print(novo_texto)

# join(), o método join() pega uma lista de strings e as juntas em uma string apenas, em um único texto. 

palavras = ["O", "garoto", "joga", "bola", "nas", "manhas", "de", "quinta"]
nova_frase = ",".join(palavras)
nova_frase_1 = "1".join(palavras)

print(nova_frase)
print(nova_frase_1)

# find(), o método find encontra a posição, índice de uma substring()

texto_2 = "O garoto gosta de correr"
print(texto_2.find("gosta"))