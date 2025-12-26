import time

class Pizza:

    def __init__(self, sabor, custo, igredientes):

        # Atributos privados, não podem ser acessados de qualquer maneira como 
        # os atributos públicos são acessados. 

        self.__sabor = sabor 
        self.__custo = custo 
        self.__igredientes = igredientes
        self.__impostos = 30 
        self.__valor = 10 
        self.__margem_lucro = 20 / 100


    # Definindo o encapslamento

    # Getters. 
    # Definindo as regras de leitura de cada atributo. 
    # Temos o encapsulamento para que eles não sejam acessados, lidos ou escritos de qualquer forma. 

    print("Lucas Soares da Silva")
    print(""" AI Student""")

    @property 
    def sabor(self):
        return self.__sabor 


    @property 
    def custo(self):
        return self.__custo 


    @property 
    def igredientes(self):
        return self.__igredientes 


    @property
    def impostos(self):
        return self.__impostos 


    @property 
    def valor(self):
        return self.__valor 


    @property 
    def margem_lucro(self):
        return self.__margem_lucro 




    # Setters 
    # Definindo as regras de escrita, uma forma que permite que o usuário possa ter uma limitação à escrita 
    # de atributos. 

    @sabor.setter 
    def sabor(self, novo_sabor):
        self.__sabor = novo_sabor


    @custo.setter 
    def custo(self, novo_custo):
        self.__custo = novo_custo


    @igredientes.setter 
    def igredientes(self, novos_igredientes):
        self.__igredientes = novos_igredientes 


    @impostos.setter 
    def impostos(self, novos_impostos):
        self.__impostos = novos_impostos 


    @valor.setter 
    def valor(self, novo_valor):
        self.__valor = novo_valor 


    @margem_lucro.setter 
    def margem_lucro(self, novo_lucro):
        self.__margem_lucro = novo_lucro 





    def alterar_sabor(self): 

        def alterando_sabor():
            while True: 

                print("Alterando o sabor da pizza de ", self.__sabor," ...")
                time.sleep(2)

                novo_sabor = input("Indique o novo sabor de pizza: ")

                confirmacao = input("Digite sim para confirmar a operção e não para nega-la: ")

                if confirmacao.lower() == "sim": 

                    print("Alterando sabor...")
                    time.sleep(2)

                    self.__sabor = novo_sabor.title()

                    break

                elif confirmacao.lower() == "não":

                    print("Alteração negada !")
                    time.sleep(2)


                else: 

                    print("Opção não identificada...")
                    time.sleep(2)

                    print("Tentando novamente...")
                    time.sleep(2)


        try: 

            alterando_sabor()

        except Exception as a: 

            print("Tentando novamente...")

            alterando_sabor()




pizza_1 = Pizza("Muzzarella", 100, \
    "Muzzarella, Cebola, Azeitona, Farinha de trigo comum, Agua gelada, sal, açucar, molho de tomate, tomate fatiado")


# Acessando atributos do objeto pizza 1. 

def testando_acesso_obj_pizza():
    sabor, custo = pizza_1.sabor, pizza_1.custo 
    print(f"Sabor da pizza {sabor}: {sabor}")
    print(f"Custo da pizza {pizza_1.sabor}: {custo}")

    print("Igredientes da pizza de " + pizza_1.sabor + ".")

    numero = 1
    for igrediente in pizza_1.igredientes:
        # String só se imprime com string, só concatenamos strings com strings. 

        print("Igrediente " + str(numero) + ": " +  igrediente)

        numero += 1

# testando_acesso_obj_pizza()


# Alterando o sabor do objeto pizza, atributo sabor. 

def testando_alterar_sabor(objeto):

    print("Sabor atual: " + objeto.sabor)

    objeto.alterar_sabor()

    print("Novo sabor: ", objeto.sabor)


testando_alterar_sabor(pizza_1)


def teetando_str():
    nome = "LUcAs"
    novo_nome = nome.title()
    nome_copia = str(novo_nome)

    print(nome.title())

    print("Novo nome:", novo_nome)
    print("Nome: ", nome)
    novo_nome = "Luca"
    print("Nome: ", nome)
    print("Nome cópia:", nome_copia)
