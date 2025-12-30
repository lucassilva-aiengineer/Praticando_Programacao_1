import time 
import funcoes 

class OperadorComum:

    """O operador é o usuário especial capaz de alterar o estoque"""

    acesso_geral = "123456"

    def __init__(self, nome= None, senha= None, id_ = None):

        self.__id_ = funcoes.gerar_id()
        self.__nome = nome 
        self.__senha = senha 
        # self.__historico_alteracoes = [] 


    # Getters, leitura
    @property 
    def id_(self):
        return self.__id_

    @property 
    def nome(self): # O próprio objeto é passado como parâmetro e dessa forma o atributo é acessado. 
        return self.__nome 


    @property 
    def senha(self):
        return self.__senha

        # tentativas = 0
        # while True:

        #     senha_acesso = input("Indique a sua senha de acesso para acessar a senha deste usuário: ")

        #     if senha_acesso == OperadorComum.acesso_geral:

        #         return self.__senha

        #     else: 

        #         tentativas += 1 
        #         print("Acesso negado!")

        #         if tentativas < 3:
        #             print("Tente novamente...")

        #             time.sleep(2)


        #         else: 

        #             print("Acesso negado!")
        #             time.sleep(2)

        #             print("Cancelando operação...")
        #             time.sleep(2)
        #             break   

    
    #  Setters, escrita. 

    @id_.setter 
    def id_(self, novo_id):
        self.__id_ = novo_id


    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome 


    @senha.setter 
    def senha(self, nova_senha):

        print("Alterando senha...")
        time.sleep(2)


        tentativas = 0
        while True: 

            tentativas += 1

            senha_acesso = input("Indique a senha de acesso: ")

            if senha_acesso == OperadorCommum.senha_acesso: 

                self.__senha = nova_senha

                print("Senha alterada com sucesso...")

                time.sleep(2)

                return "Senha alterada com sucesso."

            else: 

                if tentativas < 3:

                    print("Senha inválida.")
                    time.sleep(2)

                    print("Tente novamente...")
                    time.sleep(2)

                else: 

                    print("Acesso negado!")
                    time.sleep(2)

                    break 

