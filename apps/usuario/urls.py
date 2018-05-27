from django.conf.urls import url

from apps.usuario.views import saveCode, downloadCode, openCode, downloadCode2

urlpatterns = [
    url(r'^save-code$', saveCode, name="save_code"),
    url(r'^download/code/(?P<codeid>\d+)$', downloadCode, name="downloadCode"),
    url(r'^download/code$', downloadCode2, name="downloadCode2"),
    url(r'^(?P<idiom>[a-z]{2})/compiler/code/(?P<codeid>\d+)/$', openCode, name="openCode"),
]
