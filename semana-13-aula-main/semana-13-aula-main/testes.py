'''
Módulo testes.py - Testes unitários para a classe Turma
'''
import unittest
import aluno as a
import turma as t


class TurmaTest(unittest.TestCase):
    '''
    Testes para a classe Turma
    '''

    def setUp(self):
        '''Configuração inicial para cada teste'''
        print('Teste', self._testMethodName, 'sendo executado...')
        self.alunos = []
        self.alunos.append(a.Aluno('Fabio', 'Teixeira', 11))
        self.alunos.append(a.Aluno('Fabiano', 'Teixeira', 7))
        self.alunos.append(a.Aluno('Melissa', 'Teixeira', 8))
        self.alunos.append(a.Aluno('Rafael', 'Teixeira', 9))
        self.alunos.append(a.Aluno('Angela', 'Teixeira', 6))
        self.alunos.append(a.Aluno('Angela', 'Teixeira', -1))
        self.turma_object = t.Turma()
        self.turma_object.cadastrar_alunos(self.alunos)

    def tearDown(self):
        '''Limpeza após cada teste'''
        print('Teste', self._testMethodName, 'finalizado.')

    def test_maior(self):
        '''Testa se a maior nota é identificada corretamente'''
        self.assertEqual(9, self.turma_object.maior_nota.nota,
                         'Erro ao encontrar maior nota')

    def test_menor(self):
        '''Testa se a menor nota é identificada corretamente'''
        self.assertEqual(6, self.turma_object.menor_nota.nota,
                         'Erro ao encontrar menor nota')

    def test_intervalo(self):
        '''Testa se as notas estão no intervalo válido'''
        self.assertTrue((self.turma_object.menor_nota.nota > 0 and
                         self.turma_object.maior_nota.nota <= 10),
                        'Erro ao verificar intervalo')


if __name__ == "__main__":
    unittest.main()