from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mysite.core.views.index', name='index'),
    url(r'^contact/$', 'mysite.core.views.contact', name='contact'),
    url(r'^turma/$', 'mysite.core.views.turma', name='turma'),
   # url(r'^(?P<pk>\d+)/$', 'details', name='details'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)