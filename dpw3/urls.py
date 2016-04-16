from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$','wyswietl.views.widok'),
    url(r'^formulaz/result/$','wyswietl.views.testowywidok'),
    url(r'^formulaz/$','wyswietl.views.mainwebsite'),
    url(r'^edit/$','wyswietl.views.editProject'),
    url(r'^$','wyswietl.views.major'),
    url(r'^p0/forms/$','wyswietl.views.uoap0forms'),
    url(r'^p0/odbiorca/$','wyswietl.views.uoap0odbiorca'),
    url(r'^p0/result/$','wyswietl.views.uoapp0widok'),
    url(r'^uoap/$','wyswietl.views.uoa'),
    url(r'^p2/odbiorca/$','wyswietl.views.uoap2odbiorca'),
    url(r'^p2/forms/$','wyswietl.views.uoap2forms'),
    url(r'^p2/result/$','wyswietl.views.uoapp2widok'),


)
