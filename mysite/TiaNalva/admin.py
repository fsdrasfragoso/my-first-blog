from django.contrib import admin

from .models import Escola  

from .models import Turma

from .models import Aluno 

class EscolaAdmin(admin.ModelAdmin):
	list_display = ['inep', 'nome']
	search_fields = ['inep', 'nome']

class TurmaAdmin(admin.ModelAdmin):
	list_display = [ 'idTurma','nome', 'descricao', 'url', 'escola_inep']
	search_fields = [ 'idTurma','nome', 'escola_inep']

class AlunoAdmin(admin.ModelAdmin):
	list_display = [ 'matricula','nome', 'chamada', 'turma_idturma']
	search_fields = [ 'matricula','nome', 'chamada', 'turma_idturma']



admin.site.register(Escola, EscolaAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aluno,AlunoAdmin)
# Register your models here.
