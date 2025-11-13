'''
Módulo turma.py - Classe que representa uma turma
'''


class Turma:
    '''
    Classe que representa uma turma de alunos
    '''

    def __init__(self):
        '''Inicializa a turma com lista vazia e notas nulas'''
        self.turma = []
        self.menor_nota = None
        self.maior_nota = None

    def cadastrar_alunos(self, alunos):
        '''Cadastra alunos na turma, validando a faixa de notas'''
        for aluno in alunos:
            if 0 <= aluno.nota <= 10:
                self.turma.append(aluno)
                if self.menor_nota is None or self.menor_nota.nota > aluno.nota:
                    self.menor_nota = aluno
                if self.maior_nota is None or self.maior_nota.nota < aluno.nota:
                    self.maior_nota = aluno

    def mostrar_alunos(self):
        '''Exibe a lista de alunos da turma'''
        print('Quantidade de alunos:', len(self.turma))
        for aluno in self.turma:
            print(aluno.mostrar_aluno())
            