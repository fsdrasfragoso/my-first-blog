
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

class EscolaManager(models.Manager):
	"""docsCouseEscola models.Managerame"""
	def search(self, query):
		return self.get_queryset().filter(
			models.Q(inep_icontains=query) | \
			models.Q(nome_icontains=query)
		)
		
class TurmaManager(models.Manager):
  
  def search(self, query):
    return self.get_queryset().filter(
      models.Q(idTurma_icontains=query) | \
      models.Q(nome_icontains=query) | \
      models.Q(descricao_icontains=query)
      
      
    )

class AlunoManager(models.Manager):
  
  def search(self, query):
    return self.get_queryset().filter(
      models.Q(matricula_icontains=query) | \
      models.Q(nome_icontains=query) | \
      models.Q(chamada_icontains=query)
      
    )


class Aluno(models.Model):
    matricula = models.CharField(max_length=45,primary_key=True)
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.
    url = models.ImageField(upload_to='TiaNalva/imagem', verbose_name='imagem', null=True, blank=True)
    descricao = models.TextField(blank=True, null=True)
    chamada = models.IntegerField()
    turma_idturma = models.ForeignKey('Turma', db_column='Turma_idTurma')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aluno'
        unique_together = (('matricula'),)
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']
    def __str__(self):
      return self.nome
    





class Assunto(models.Model):
    idAssunto = models.IntegerField(db_column='idAssunto', blank=True, primary_key=True)
    assunto = models.CharField(db_column='Assunto', max_length=45, )  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=45, blank=True, null=True)  # Field name made lowercase.
    disciplina_iddisciplina = models.ForeignKey('Disciplina', db_column='Disciplina_idDisciplina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assunto'
        unique_together = (('idAssunto'),)
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'
        ordering = ['assunto']
    def __str__(self):
      return self.assunto
    
    



class Disciplina(models.Model):
    iddisciplina = models.IntegerField(db_column='idDisciplina', blank=True, primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45, blank=True, null=True)  # Field name made lowercase.
    turma_idturma = models.ForeignKey('Turma', db_column='Turma_idTurma')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disciplina'
       # unique_together = (('idDisciplina'),)
    
class AlunoHasDisciplina(models.Model):
    id = models.IntegerField(db_column='id', blank=True, primary_key=True)
    aluno_matricula = models.ForeignKey(Aluno, db_column='ALUNO_matricula')  # Field name made lowercase.
    disciplina_iddisciplina = models.ForeignKey('Disciplina', db_column='Disciplina_idDisciplina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aluno_has_disciplina'
        unique_together = (('id'),)



class Escola(models.Model):
    inep = models.CharField(primary_key=True, max_length=100)
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'escola'
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'
        ordering = ['nome']
    def __str__(self):
      return self.nome
    

class Medias(models.Model):
  #  id = models.AutoField()
    primeiro_bimestre = models.FloatField()
    segundo_bimestre = models.FloatField()
    terceiro_bimestre = models.FloatField()
    quarto_bimestre = models.FloatField()
    resultado = models.FloatField(blank=True, null=True)
   # aluno_has_disciplina = models.ForeignKey(AlunoHasDisciplina, db_column='Aluno_has_Disciplina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medias'
    #    unique_together = (('id', 'Aluno_has_Disciplina_id'),)


class Nota01(models.Model):
   # idnota01 = models.AutoField(db_column='idNota01')  # Field name made lowercase.
    nota = models.FloatField()
    #aluno_has_disciplina = models.ForeignKey(AlunoHasDisciplina, db_column='Aluno_has_Disciplina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nota01'
     #   unique_together = (('idNota01', 'Aluno_has_Disciplina_id'),)


class Nota02(models.Model):
 #   id = models.AutoField()
    nota = models.FloatField(db_column='Nota')  # Field name made lowercase.
 #   aluno_has_disciplina = models.ForeignKey(AlunoHasDisciplina, db_column='Aluno_has_Disciplina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nota02'
  #      unique_together = (('id', 'Aluno_has_Disciplina_id'),)


class Nota03(models.Model):
  #  id = models.AutoField()
    nota = models.FloatField()
   # aluno_has_disciplina = models.ForeignKey(AlunoHasDisciplina, db_column='Aluno_has_Disciplina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nota03'
    #    unique_together = (('id', 'Aluno_has_Disciplina_id'),)


class Nota04(models.Model):
   # id = models.AutoField()
    nota = models.FloatField()
   # aluno_has_disciplina = models.ForeignKey(AlunoHasDisciplina, db_column='Aluno_has_Disciplina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nota04'
    #    unique_together = (('id', 'Aluno_has_Disciplina_id'),)


class Nota05(models.Model):
  #  id = models.AutoField()
    nota = models.FloatField()
   # aluno_has_disciplina = models.ForeignKey(AlunoHasDisciplina, db_column='Aluno_has_Disciplina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nota05'
    #    unique_together = (('id', 'Aluno_has_Disciplina_id'),)


class Nota06(models.Model):
  #  id = models.AutoField()
    nota = models.FloatField()
   # aluno_has_disciplina = models.ForeignKey(AlunoHasDisciplina, db_column='Aluno_has_Disciplina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nota06'
    #    unique_together = (('id', 'Aluno_has_Disciplina_id'),)


class Nota07(models.Model):
   # id = models.AutoField()
    nota = models.FloatField(db_column='Nota')  # Field name made lowercase.
    #aluno_has_disciplina = models.ForeignKey(AlunoHasDisciplina, db_column='Aluno_has_Disciplina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nota07'
     #   unique_together = (('id', 'Aluno_has_Disciplina_id'),)


class Nota08(models.Model):
   # id = models.AutoField()
    nota = models.CharField(db_column='Nota', max_length=45)  # Field name made lowercase.
   # aluno_has_disciplina = models.ForeignKey(AlunoHasDisciplina, db_column='Aluno_has_Disciplina_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nota08'
    #    unique_together = (('id', 'Aluno_has_Disciplina_id'),)


class Questao(models.Model):
    idquestao = models.IntegerField(db_column='idQuestao',  blank=True, primary_key=True) # Field name made lowercase.
    pergunta = models.TextField()
    resposta = models.TextField(db_column='Resposta')  # Field name made lowercase.
    score = models.FloatField(db_column='Score')  # Field name made lowercase.
    nivel = models.IntegerField(db_column='Nivel')  # Field name made lowercase.
    assunto_idassunto = models.ForeignKey(Assunto, db_column='Assunto_idAssunto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questao'
#        unique_together = (('idQuestao', 'Assunto_idAssunto'),)

class Ranking(models.Model):
  #  idranking = models.AutoField(db_column='idRanking')  # Field name made lowercase.
    pontuacao = models.FloatField()
  #  aluno_matricula = models.ForeignKey(Aluno, db_column='ALUNO_matricula')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ranking'
   #     unique_together = (('idRanking', 'ALUNO_matricula'),)

class Turma(models.Model):
    idTurma = models.IntegerField(db_column='idTurma',  blank=True, primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    url = models.ImageField(upload_to='TiaNalva/imagem', verbose_name='imagem', null=True, blank=True)
    escola_inep = models.ForeignKey(Escola, db_column='ESCOLA_inep')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turma'
        unique_together = (('idTurma'),)
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['nome']
    def __str__(self):
      return self.nome
    

    #def (self):
     # return self__str__.nome

# fazer alteração aqui
class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario',blank=True, primary_key=True)  # Field name made lowercase.
    nivel = models.IntegerField(db_column='nivel', blank=False, null=False)
    cadastro = models.DateField(blank=True, null=True, default=timezone.now)
    escola_inep = models.ForeignKey(Escola, db_column='ESCOLA_inep')  
    usuario = models.ForeignKey(User,null=False, blank=False, related_name='+')
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('idusuario'),)

@models.permalink
def get_absolute_url(self):
  return reverse('details', args=(self.idTurma,))


objects = EscolaManager()

objects = TurmaManager()
objects = AlunoManager()


