from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mysite.core.views.index', name='index'),
    url(r'^contact/$', 'mysite.core.views.contact', name='contact'),
    url(r'^turma/$', 'mysite.core.views.turma', name='turma'),
    url(r'^admin/', include(admin.site.urls)),
)
