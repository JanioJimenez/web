from django.conf.urls import url

from apps.page.views import home

urlpatterns = [
    url(r'^(?P<idiom>[a-z]{2})/$', home, name="home"),
    url(r'^$', home, name="home"),
    # url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),

]
