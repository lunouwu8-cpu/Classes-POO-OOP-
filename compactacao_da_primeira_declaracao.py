#Declaração de classe
class Gafanhoto:
    #Manual da classe
    """Essa classe cria um gafanhoto que é uma pessoa que tem nomes, idades, sexo, se está vivo ou morto e se está usando roupa ou não.
    
    Para criar uma nova pessoa(Gafanhoto), use
    variavél = Gafanhoto(nome, idade, sexo)"""
    #Construtor da classe
    def __init__(self, nome="Vazio", idade=0, sexo="Unissex"):
        #Atributos de instância
        self.nome = nome
        self.idade = idade
        self.vivo = True
        self.sexo= sexo
        self.roupa = True
    #Método de instância
    def aniversario(self):
        self.idade +=1
    def tirar_roupa(self):
        self.roupa = False

    def matar(self):
        self.vivo = False
    def __str__(self):
        return f'{self.nome} é gafanhoto e tem {self.idade} anos de idade é do sexo {self.sexo} e está {"vivo" if self.vivo else "morto"}. Ele está {"usando roupa. Tudo certo!" if self.roupa else "sem roupa. Sem vergonha!"}'
    def __getstate__(self):
        return f"Estado: Nome = {self.nome}, Idade = {self.idade}, Sexo = {self.sexo}, Vivo = {self.vivo}, Roupa = {self.roupa}"
#nome do objeto e chamada do construtor da classe + atribuição de atributos
gafanhoto1 = Gafanhoto(nome="Lucas", idade=20, sexo="Masculino")
gafanhoto1.aniversario()
#print(gafanhoto1())
print(gafanhoto1.__getstate__()) #É um método de instância.
print(gafanhoto1.__dict__) #É um atributo.
print(gafanhoto1.__class__) #É um atributo.
#print(gafanhoto1.__doc__) Dunder attribute = atributo de instância