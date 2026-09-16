#Declaração de classe
class Gafanhoto:
    #Construtor da classe
    def __init__(self):
        #Atributos de instância
        self.nome = ""
        self.idade = 0
        self.vivo = True
        self.sexo= ""
        self.roupa = True
    #Método de instância
    def aniversario(self):
        self.idade +=1
    def tirar_roupa(self):
        self.roupa = False

    def matar(self):
        self.vivo = False
    

    def menssagem(self):
        return f'{self.nome} é gafanhoto e tem {self.idade} anos de idade é do sexo {self.sexo} e está {"vivo" if self.vivo else "morto"}. Ele está {"usando roupa. Tudo certo!" if self.roupa else "sem roupa. Sem vergonha!"}'
#Declaração de objeto
#nome do objeto e chamada do construtor da classe
gafanhoto1 = Gafanhoto()
#Atributos:
gafanhoto1.nome = "Lucas"
gafanhoto1.idade = 20
gafanhoto1.sexo = "Masculino"
#métodos:
gafanhoto1.aniversario()
#chamada do construtor da classe
gafanhoto2 = Gafanhoto()
#Atributos:
gafanhoto2.nome = "Ana"
gafanhoto2.idade = 17
gafanhoto2.sexo = "Feminino"
#métodos:
gafanhoto2.tirar_roupa()
gafanhoto2.matar()
#chamada do construtor da classe
gafanhoto3 = Gafanhoto()
#Atributos:
gafanhoto3.nome = "Bruna"
gafanhoto3.idade = 145
gafanhoto3.sexo = "Feminino"
#métodos:
gafanhoto3.matar()
print(gafanhoto1.menssagem())
print(gafanhoto2.menssagem())
print(gafanhoto3.menssagem())