class Usuario: 

    """ Classe usuário, que define o objeto usuário por meio de métodos 
    e atributos, e tem um método que permite inserir produtos no estoque."""

    def __init__(self, estoque= None, nome= None, nome_user= None, senha= None, status= False):


    # Atributos privados. 
        self.__estoque = estoque
        self.__nome = nome 
        self.__nome_user = nome_user 
        self.__senha = senha 
        self.__status = False

    # Organisando o encapslamento 


    # Getters 

    # Desenvolvendo uma lógica de leitura segura para o atributo. 
    @property 
    def nome(self):
        return self.__nome

    @property 
    def nome_user(self):
        return self.__senha 

    @property 
    def senha(self):
        return self.__status

    @property 
    def status(self):
        return self.__status 


    # Desenvolvendo os setters, que nos permitem alterar os atributos, cria uma lógica 
    # de escrita. 

    @nome.setter 
    def nome(self, novo_nome):

        self.__nome = novo_nome
        print("Nome alterado com sucesso!")


    @nome_user.setter 
    def nome_user(self, novo_nome_usuario):

        self.__nome_user = novo_nome_usuario 
        print("Nome de usuário alterado com sucesso!")


    @senha.setter 
    def senha(self, nova_senha):

        self.__senha = nova_senha 
        print("Senha alterada com sucesso!")


    @status.setter 
    def status(self, novo_status):

        self.__status = novo_status     
        print("Status alterado com sucesso!")



# Criando um objeto usuario. 

# Como estamos utilizando argumentos de palavra chave podemos omitir alguns que no caso 
# terá valor None atribuído, e nós atribuímos cada atribuido ao nome que é esperado na 
# função. 

usuario = Usuario(nome= "Lucas", nome_user="lucass001", senha= "1234", status= True)

print(usuario.nome)