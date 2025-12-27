class Roupa:

    def __init__(self, modelo, marca, tamanho, cor, quantidade):

        # Atributos privados 
        self.__modelo = modelo
        self.__marca = marca   
        self.__tamanho = tamanho 
        self.__cor = cor 
        self.__quantidade = quantidade

    # Definindo o encapsulamento.
    # Defindo os getters, a lógica de leitura. 
    # O encapsulamento serve para proteger o acesso aos atributos, tanto em relação a 
    # escrita como em relação a leitura. 

    @property
    def modelo(self): # Nós temos o próprio objeto como parâmetro da função e acessamos o atributo deste. 
        # Definindo uma lógica especial de acesso.


        # Para isto 
        modelo_mostrar = ""

        caracteres_acrescentados = 0
        for caracter in self.__modelo:

            if caracteres_acrescentados >= 5:

                if caracter == " ":
                    modelo_mostrar += "-"


                else:

                    modelo_mostrar += "*"

            else: 

                modelo_mostrar += caracter

            caracteres_acrescentados += 1

        return modelo_mostrar


    @property 
    def marca(self):
        return self.__marca 


    @property 
    def tamanho(self):
        return self.__tamanho 


    @property 
    def cor(self):
        return self.__cor 

    
    @property 
    def quantidade(self):
        return self.__quantidade 



    # Defindo uma regra especial de escrita, os setters. 
    @modelo.setter 
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo 


    @marca.setter 
    def marca(self, nova_marca):
        self.__marca = nova_marca 


    @tamanho.setter 
    def tamanho(self, novo_tamanho):
        self.__tamanho = novo_tamanho 


    @cor.setter 
    def cor(self, nova_cor):
        self.__cor = nova_cor 


    @quantidade.setter 
    def quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade 

# Testando o molde dos objetos que serão criados, e possuiram os próprios atributos e 
# os próprios métodos que modificaram os próprios atributos. 

# objeto_teste 
# Ativa o método construtor e aloca espaço na memória para os atributos e recebe os argumentos do método construtor 
# nos atributos, e cria o objeto com próprios atributos e métodos. 

def testando_objeto():
    roupa_1 = Roupa("Blazer (acompanha gravata)", "High-Still", "GG", "Preto")

    print(roupa_1.modelo)



def testando_string():

    string_teste = "O meu nome cpf é 123 456 789 10"

    nova_string = ""
    caracteres_exibidos = 0
    for caracter in string_teste:

        if caracteres_exibidos >= 3:
            if caracter == " ":

                nova_string += "-"

            else: 
                nova_string += "*"


        else: 

            nova_string += caracter 

        caracteres_exibidos += 1

    print(nova_string)