from django.shortcuts import render, get_object_or_404, redirect, render_to_response, RequestContext
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings

from TiaNalva.models import Turma, Disciplina, AlunoHasDisciplina, Aluno, Usuario, Assunto
from TiaNalva.forms import ContactTurma, FormTurma, FormAluno 
from TiaNalva.forms import RegisterForm, EditAccountForm, FormDisciplina
from TiaNalva.forms import FormAssunto, FormQuestao
import json


def registrar(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            a = Assunto()
            a.assunto = request.POST.get('id_nome')
            a.descricao = request.POST.get('id_descricao')
            a.disciplina_iddisciplina = request.POST.get('idDiciplina')
            a.save()
            #print("Assunto: "+ a.descricao)
            #print("Disciplina: "+ a.disciplina_iddisciplina)
            return HttpResponse(json.dumps(True), content_type="application/json")
            return HttpResponse(json.dumps(False), content_type="application/json")
        except Exception as e:
            return HttpResponse(json.dumps(False), content_type="application/json")
    raise Http404





def return_disciplina(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            if request.POST.get('id') != "":
                turma = get_object_or_404(Turma,pk=request.POST.get('id'))
                disciplinas = Disciplina.objects.filter(turma_idturma=turma)
                objeto_retornado = []
                for i in disciplinas:
                    objeto_retornado.append([i.pk,i.nome])
                return HttpResponse(json.dumps(objeto_retornado), content_type="application/json")
            return HttpResponse(json.dumps(False), content_type="application/json")
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps(False), content_type="application/json")
    raise Http404

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def contact(request):
	return render(request, 'contact.html')

@login_required
def turma(request):
	turmas = Turma.objects.all()
	context = {
		'turmas': turmas
	}
	return render(request, 'turma.html', context)	

@login_required
def CadastrarAssunto(request):
    turmas = Turma.objects.all()
    disciplinas = Disciplina.objects.all()
    context = {}
    context['turmas'] = turmas
    context['disciplinas'] = disciplinas

    # Cria form
    form = FormAssunto(request.POST or None)
 
    # Valida e salva
    if form.is_valid():
        
        salvar = form.save(commit=False)
        salvar.save()
        return HttpResponse("Dados inseridos com sucesso!")        
 
    # Chama Template
    return render(request, 'Assunto.html', context)

#def details(request, pk):
#	turma = get_object_or_404(Turma, pk=pk)
#	context = {
#		'turma': turma
#	}
#	 
#	return render(request, 'details.html', context)
@login_required
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


@login_required
def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)

def register(request):
        
    if request.method == 'POST' and request.is_ajax():
        userInstance = User()
        userInstance.username = request.POST.get('username')
        
        passw = request.POST.get('password')
        userInstance.set_password(passw)
        userInstance.save()
        print("user: "+ userInstance.username)
        print("senha: "+ passw)
        

        user = authenticate(username=userInstance.username, password=passw)
        if user is not None:
            if user.is_active:
                login(request, user)
                usuario = Usuario()
                usuario.nivel = request.POST.get('nivel')
                usuario.escola_inep = request.POST.get('escola_inep')
                usuario.save()
                return HttpResponse(json.dumps(True), content_type="application/json")
        return HttpResponse(json.dumps(False), content_type="application/json")
    raise Http404

@login_required
def edit(request):
    template_name = 'edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def edit_password(request):
    template_name = 'edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def CadastrarQuestao(request):
    request.user
    # Cria form
    form = FormQuestao(request.POST or None)
 
    # Valida e salva
    if form.is_valid():
        
        salvar = form.save(commit=False)
        salvar.save()
        return HttpResponse("Dados inseridos com sucesso!")        
 
    # Chama Template
    return render_to_response("Cadastro.html",
                              locals(),
                              context_instance = RequestContext(request))




@login_required
def CadastrarTurma(request):
    request.user
    # Cria form
    form = FormTurma(request.POST or None)
 
    # Valida e salva
    if form.is_valid():
        
        salvar = form.save(commit=False)
        salvar.save()
        return HttpResponse("Dados inseridos com sucesso!")        
 
    # Chama Template
    return render_to_response("Cadastro.html",
                              locals(),
                              context_instance = RequestContext(request))

@login_required
def CadastrarAluno(request):
 
    # Cria form
    form = FormAluno(request.POST or None)
 
    # Valida e salva
    if form.is_valid():
        
        salvar = form.save(commit=False)
        salvar.save()
        disc = Disciplina.objects.filter(turma_idturma=salvar.turma_idturma)
        for disciplina in disc:
            newhas = AlunoHasDisciplina()
            newhas.aluno_matricula = salvar
            newhas.disciplina_iddisciplina = disciplina
            newhas.save()

        return HttpResponse("Dados inseridos com sucesso!")        
 
    # Chama Template
    return render_to_response("Cadastro.html",
                              locals(),
                              context_instance = RequestContext(request))


@login_required
def CadastrarDisciplina(request):
 
    # Cria form
    form = FormDisciplina(request.POST or None)
 
    # Valida e salva
    if form.is_valid():
        
        salvar = form.save(commit=False)
        salvar.save()
        a = Disciplina.objects.last()
        alun = Aluno.objects.filter(turma_idturma=salvar.turma_idturma)
        for aluno in alun:
            newhas = AlunoHasDisciplina()
            newhas.aluno_matricula = aluno
            newhas.disciplina_iddisciplina = a
            newhas.save()


        return HttpResponse("Dados inseridos com sucesso!")        
 
    # Chama Template
    return render_to_response("Cadastro.html",
                              locals(),
                              context_instance = RequestContext(request))


