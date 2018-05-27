# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from apps.page.models import Idiom
from apps.usuario.models import Code
from apps.usuario.forms import CodeForm

# Create your views here.

def saveCode(request):
    form = CodeForm(request.POST)
    # return HttpResponse(form)
    if form.is_valid():
        form.save()

    return HttpResponseRedirect(reverse_lazy('page:redirect',  args=['es', 'mycodes']))

def downloadCode(request, codeid):
    code = Code.objects.get(id=codeid)
    return HttpResponse(code.code)

def downloadCode2(request):
    archivo = open("static/codigo-descarga.txt","w")
    archivo.write(request.POST['code'])
    archivo.close()
    return HttpResponseRedirect(reverse_lazy('page:redirect',  args=['es', 'downloadcode']))


def openCode(request, idiom, codeid):
    language = Idiom.objects.filter(min_name=idiom).first()

    if language:
        idioms = Idiom.objects.all()
        context = {"language" : language, "idioms":idioms}

        code = Code.objects.get(id=codeid)
        context.setdefault("code", code)

        return render(request, 'page/compiler.html', context)
    else:
        return HttpResponse("El idioma no fue encontrado");
