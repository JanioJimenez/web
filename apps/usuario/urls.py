from django.conf.urls import url

from apps.usuario.views import saveCode, openCode

urlpatterns = [
    url(r'^save-code$', saveCode, name="save_code"),
    url(r'^(?P<idiom>[a-z]{2})/compiler/code/(?P<codeid>\d+)/$', openCode, name="openCode"),
]
