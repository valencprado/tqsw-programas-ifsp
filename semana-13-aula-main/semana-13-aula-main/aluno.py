class Aluno:
  def __init__(self, nome, sobrenome, nota):
    self.nome = nome
    self.sobrenome = sobrenome
    self.nota = nota

  def mostrar_aluno(self):
    '''
    Retorna informações do aluno.
    '''
    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota)
  