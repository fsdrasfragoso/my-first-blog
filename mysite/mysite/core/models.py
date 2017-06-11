from __future__ import unicode_literals

from django.db import models


class Turma(models.Model):
    idTurma = models.IntegerField(db_column='idTurma',  blank=True, primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(blank=True, null=True)
    url = models.ImageField(upload_to='TiaNalva/images', verbose_name='imagem', null=True, blank=True)
    escola_inep = models.ForeignKey(Escola, db_column='ESCOLA_inep')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turma'
        unique_together = (('idTurma'),)
