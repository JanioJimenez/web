from django.conf.urls import url

from apps.page.views import home, UserRegister

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^(?P<idiom>[a-z]{2})/$', home, name="home"),
    url(r'^signup', UserRegister.as_view(), name="signup"),

]
