from django.shortcuts import render, get_object_or_404
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


def details(request, pk):
	turma = get_object_or_404(Turma, pk=pk)
	context = {
		'turma': turma
	}
	 
	return render(request, 'details.html', context)

