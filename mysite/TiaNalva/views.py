    
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from .forms import MeuForm


def index(request):
 
    # Cria form
    form = MeuForm(request.POST or None)
 
    # Valida e salva
    if form.is_valid():
        inep = form.field(commit='INEP')
        nome = form.field(commit='Nome da Escola')
        salvar = form.save(commit=False)
        salvar.save()
        return HttpResponse("Dados inseridos com sucesso!")        
 
    # Chama Template
    return render_to_response("index.html",
                              locals(),
                              context_instance = RequestContext(request))






# Create your views here.
