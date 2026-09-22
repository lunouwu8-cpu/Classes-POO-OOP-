from abc import ABC, abstractmethod #Abstract base class
from rich import inspect
class veiculos(ABC):
    def __init__(self, nome="", numero=0):
        self.nome = nome
        self.numero = numero
    def buzinar(self):
        print(f"O veículo buzinou")
    @abstractmethod
    def andar(self):
        pass
class moto(veiculos):
    def __init__(self, nome, numero, valor=0):
        super().__init__(nome, numero)
        self.valor = valor
    def correr(self):
        print("A moto acelerou.")
    def andar(self):
        print("A moto está andando.")
class carro(veiculos):
    def __init__(self, nome, numero, valor=0):
        super().__init__(nome, numero)
        self.valor = valor
    def correr(self):
        print("O carro acelerou.")
    #def andar(self):
        #print("O carro está rodando.")
class navio(veiculos):
    def __init__(self, nome, numero, valor=0):
        super().__init__(nome, numero)
        self.valor = valor
    def correr(self):
        print("O navio acelerou.")
    def andar(self):
        print("O navio está navegando.")
m1=moto(nome="yamaha", numero= 90, valor=2000)
m1.buzinar()
m1.correr()
c1=carro(nome="toyota", numero=100, valor=3000)
c1.buzinar()
c1.correr()
n1=navio(nome="Titanic", numero=200, valor=5000)
n1.buzinar()
n1.correr()