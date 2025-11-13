'''
Módulo main.py - Executa o sistema de gerenciamento de turmas
'''
import aluno as a
import turma as t

alunos = []
alunos.append(a.Aluno('Fabio', 'Teixeira', 11))
alunos.append(a.Aluno('Fabiano', 'Teixeira', 7))
alunos.append(a.Aluno('Melissa', 'Teixeira', 8))
alunos.append(a.Aluno('Rafael', 'Teixeira', 9))
alunos.append(a.Aluno('Angela', 'Teixeira', 6))

turma_object = t.Turma()
turma_object.cadastrar_alunos(alunos)

turma_object.mostrar_alunos()
print('*'*30)
print('Aluno com menor nota:', turma_object.menor_nota.mostrar_aluno())
print('Aluno com maior nota:', turma_object.maior_nota.mostrar_aluno())
turma_object.maior_nota.mostrar_aluno()
