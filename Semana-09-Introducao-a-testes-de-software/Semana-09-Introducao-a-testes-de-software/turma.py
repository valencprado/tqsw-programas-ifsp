class Turma:
  def __init__(self):
    self.turma = []
    self.menorNota = None
    self.maiorNota = None

  def cadastrarAlunos(self, alunos):    
    for i in alunos:
      if(i.nota >= 0 and i.nota <= 10):
        if((self.menorNota == None) or (self.menorNota.nota > i.nota)):
          self.menorNota = i
        if((self.maiorNota == None) or (self.maiorNota.nota < i.nota)):
          self.maiorNota = i          
        self.turma.append(i)
      else:
        print('Nota inválida para o aluno:', i.mostrarAluno())

  def mostrarAlunos(self):  
    print('Quantidade de alunos:', len(self.turma))
    for x in self.turma:      
      print(x.mostrarAluno())