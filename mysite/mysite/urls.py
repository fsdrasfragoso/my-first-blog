from django.conf.urls import url, include, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','mysite.core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

)
from django.conf.urls import url, include, patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','mysite.core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

)
