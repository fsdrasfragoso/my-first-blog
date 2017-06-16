from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings

from TiaNalva.models import Turma
from TiaNalva.forms import ContactTurma
from TiaNalva.forms import RegisterForm, EditAccountForm


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


@login_required
def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)

def register(request):
    template_name = 'register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

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