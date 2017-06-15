from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from TiaNalva.models import Turma
from TiaNalva.forms import ContactTurma



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


#def details(request, pk):
#	turma = get_object_or_404(Turma, pk=pk)
#	context = {
#		'turma': turma
#	}
#	 
#	return render(request, 'details.html', context)

def details(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    context = {}
    if request.method == 'POST':
        form = ContactTurma(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(turma)
            form = ContactTurma()
    else:
        form = ContactTurma()
    context['form'] = form
    context['turma'] = turma
    template_name = 'details.html'
    return render(request, template_name, context)
