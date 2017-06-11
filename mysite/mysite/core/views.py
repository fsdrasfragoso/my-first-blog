from django.shortcuts import render
from django.http import HttpResponse

from TiaNalva.models import Turma

def index(request):
    return render(request, 'index.html')


def contact(request):
	return render(request, 'contact.html')


def turma(request):
	turmas = Turma.objects.all()
	context = {
		'turmas': turmas
	}
	return render(request, 'turma.html', context)	

"""
def details(request, pk):
	turma = Turma.objects.get(pk=pk)
	context = {
		'turma': turma
	}
	template_name = 'details.html'
	return render(request, template_name, context)

"""