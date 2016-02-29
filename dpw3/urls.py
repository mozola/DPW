from django.conf.urls import patterns, include, url
from django.contrib import admin
#from .views import widok
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dpw3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$','wyswietl.views.widok'),
    url(r'^test2/$','wyswietl.views.testowywidok'),
    url(r'^$','wyswietl.views.mainwebsite'),
    url(r'^edit/$','wyswietl.views.editProject'),
)
