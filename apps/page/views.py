from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from apps.page.models import Idiom, Info

def home(request, idiom="es"):
	idiom = Idiom.objects.filter(min_name=idiom).first()

	if idiom:
		idioms = Idiom.objects.all()

		context = {"language" : idiom, "idioms":idioms}
		# return HttpResponse(idiom.info.title);
		return render(request, 'page/home.html', context)
	else:
		return HttpResponse("El idioma no fue encontrado");
