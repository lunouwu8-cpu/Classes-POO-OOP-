from rich import inspect
class pessoa:
    def __init__(self, nome='', idade=0):
       self.nome= nome
       self.idade = idade
    def fazer_aniversario(self):
        self.idade += 1
class aluno(pessoa):
    def __init__(self,nome, idade, curso='', turma=''):
        super().__init__(nome, idade)
        self.curso= curso
        self.turma= turma
    def fazer_matricula():
        pass
class professor(pessoa):
    def __init__(self, nome, idade, especialidade='', nivel=''):
        super().__init__(nome, idade)# Usei as caracteristicas e comportamentos da Superclasse Pessoa.
        self.especialidade = especialidade
        self.nivel= nivel
    def dar_aula():
        pass

a1=aluno(idade=10, nome='josé',curso='bombeiros', turma='10-O' )
a1.fazer_aniversario()
inspect(a1, methods=True)# Usar "Methods=True" me mostra os metodos que posso usar.