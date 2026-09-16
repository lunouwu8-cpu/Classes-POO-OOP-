from rich import inspect, print
class contabanco:
    """Aqui pegamos seus dados e somamos"""
    def __init__(self, conta='vazio', titular='nenhum', grana=0):
        self.conta= conta
        self.titular= titular
        self.grana=grana
        print(f' Conta {self.conta} criada com sucesso!')
    def __str__(self):
        return f""" -----dados-----
        Número da conta: {self.conta}.
        Titular: {self.titular}.
        Saldo: R$ {self.grana:,.2f}"""
    def depositar(self, valor):
        self.grana += valor
        print(f'Depósito autorizado de valor R$: {valor:,.2f} na conta {self.conta}')
    def sacar(self, valor):
        if valor > self.grana:
            print(f"Saque de {valor} NEGADO! saldo insuficiente(Saldo atual={self.grana:,.2f})")
        else:
            self.grana -= valor 
            print(f'Saque autorizado de valor {valor:,.2f} na conta {self.conta}')

conta1= contabanco(conta=145, titular="lucas", grana=5000)
conta1.depositar(1000)
conta1.sacar(3005000)
inspect(conta1)
    