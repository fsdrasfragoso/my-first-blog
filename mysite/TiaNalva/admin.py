from django.contrib import admin

from .models import Escola

class EscolaAdmin(admin.ModelAdmin):
	list_display = ['inep', 'nome']
	search_fields = ['inep', 'nome']

admin.site.register(Escola, EscolaAdmin)

# Register your models here.
