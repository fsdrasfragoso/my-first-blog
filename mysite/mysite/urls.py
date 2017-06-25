from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mysite.core.views.index', name='index'),
    url(r'^contact/$', 'mysite.core.views.contact', name='contact'),
    url(r'^turma/$', 'mysite.core.views.turma', name='turma'),
    url(r'^Cadastro/turma/$', 'mysite.core.views.CadastrarTurma', name='CadastrarTurma'),
    url(r'^Cadastro/Aluno/$', 'mysite.core.views.CadastrarAluno', name='CadastrarAluno'),
    url(r'^Cadastro/Assunto/$', 'mysite.core.views.CadastrarAssunto', name='CadastrarAssunto'),
    url(r'^Cadastro/Questao/$', 'mysite.core.views.CadastrarQuestao', name='CadastrarQuestao'),
    url(r'^registrar/$', 'mysite.core.views.registrar', name='registrar'),
    url(r'^return_disciplina/$', 'mysite.core.views.return_disciplina', name='return_disciplina'),
    url(r'^Cadastro/Disciplina/$', 'mysite.core.views.CadastrarDisciplina', name='CadastrarDisciplina'),
    url(r'^turma/(?P<pk>\d+)/$', 'mysite.core.views.details', name='details'),
    url(r'^painel/$', 'mysite.core.views.dashboard', name='dashboard'),
    url(r'^entrar/$', 'django.contrib.auth.views.login', 
        {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', 'django.contrib.auth.views.logout', 
        {'next_page': 'index'}, name='logout'),
    url(r'^cadastre-se/$', 'mysite.core.views.register', 
        name='register'),
    url(r'^editar/$', 'mysite.core.views.edit', 
        name='edit'),
    url(r'^editar-senha/$', 'mysite.core.views.edit_password', 
        name='edit_password'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)