from django.conf.urls import url

from apps.page.views import home, redirect, UserRegister, user_complete_register, test

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^test$', test, name="test"),
    url(r'^(?P<idiom>[a-z]{2})/$', home, name="home"),
    url(r'^signup/$', UserRegister.as_view(), name="signup"),
    url(r'^(?P<idiom>[a-z]{2})/(?P<pagename>[a-z]{,20})/complete-register$', user_complete_register, name="complete_register"),
    # url(r'^page/(?P<idiom>\w+)/(?P<pagename>\w+)$', redirect, name="redirect"),
    url(r'^(?P<idiom>[a-z]{2})/(?P<pagename>[a-z]{,20})$', redirect, name="redirect"),
]
