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