from django.contrib import admin

from .models import Escola  

from .models import Turma


class EscolaAdmin(admin.ModelAdmin):
	list_display = ['inep', 'nome']
	search_fields = ['inep', 'nome']

class TurmaAdmin(admin.ModelAdmin):
	list_display = [ 'idTurma','nome', 'descricao', 'url', 'escola_inep']
	search_fields = [ 'idTurma','nome', 'escola_inep']


admin.site.register(Escola, EscolaAdmin)
admin.site.register(Turma, TurmaAdmin)
# Register your models here.
