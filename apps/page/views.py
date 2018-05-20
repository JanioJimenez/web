from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from apps.page.models import Idiom

def home(request, idiom="es"):
	idioms = Idiom.objects.all()
	idiom = Idiom.objects.filter(min_name=idiom).first()

	if idiom:
		context = {"language" : idiom, "idioms":idioms}
		# return HttpResponse(idiom.min_name);
		return render(request, 'page/home.html', context)
	else:
		return HttpResponse("El idioma no fue encontrado");
