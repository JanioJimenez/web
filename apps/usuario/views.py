# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DeleteView

from apps.page.models import Idiom
from apps.usuario.models import Code, User, City
from apps.usuario.forms import CodeForm, UserUpdateForm, CityForm,\
    UserUpdatePasswordForm, UserRegisterForm

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth.decorators import login_required

@login_required
def saveCode(request):
    form = CodeForm(request.POST)
    if form.is_valid():
        form.save()

    return HttpResponseRedirect(reverse_lazy('page:redirect',  args=['es', 'mycodes']))

@login_required
def downloadCode(request, codeid):
    code = Code.objects.get(id=codeid)
    return HttpResponse(code.code)

@login_required
def downloadCode2(request):
    archivo = open("static/codigo-descarga.txt","w")
    archivo.write(request.POST['code'])
    archivo.close()
    return HttpResponseRedirect(reverse_lazy('page:redirect',  args=['es', 'downloadcode']))

@login_required
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

@login_required
def userUpdate(request, idiom):
    language = Idiom.objects.filter(min_name=idiom).first()
    user = User.objects.get(id=request.user.id)
    if language:
    	idioms = Idiom.objects.all()

    	if request.method == 'POST':

    		form = UserUpdateForm(request.POST, instance=user)
    		# form = UserUpdateForm(request.POST)
    		form2 = CityForm(request.POST, instance=user.city)

    		print('form.is_valid()------->',form.is_valid())
    		print('form2.is_valid()------->',form2.is_valid())
    		if form.is_valid() and form2.is_valid():
    			# user = form.save(commit=False)
    			print('--------> Es valido se guardaran los cambios')

    			user.city = form2.save()
    			user.save()

    		return HttpResponseRedirect(reverse_lazy('page:redirect',  args=[idiom, 'profile']))
    	else:
    		form = UserUpdateForm(instance=user)
    		form2 = CityForm(instance=user.city)

    	return render(request, 'user/update-form.html', {"language" : language, "idioms":idioms, 'form':form, 'form2':form2})
    else:
    	return HttpResponse("El idioma no fue encontrado");

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            print(">>>> Se cambio la contraseña")
            return redirect('login')
        else:
            print(">>>> contraseña no cambiada")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/changePassword.html', {'form': form})


class UserDelete(DeleteView):
	model = User
	template_name = 'user/deleteAccount.html'
	success_url = reverse_lazy('login')
