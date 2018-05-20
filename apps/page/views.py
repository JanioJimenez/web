from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.models import User
from django.views.generic import CreateView

from apps.page.models import Idiom, Info
from apps.usuario.forms import UserRegisterForm, CityForm

def home(request, idiom="es"):
	idiom = Idiom.objects.filter(min_name=idiom).first()

	if idiom:
		idioms = Idiom.objects.all()

		context = {"language" : idiom, "idioms":idioms}
		# return HttpResponse(idiom.info.title);
		return render(request, 'page/home.html', context)
	else:
		return HttpResponse("El idioma no fue encontrado");

class UserRegister(CreateView):
	model = User
	template_name = 'user/register.html'
	form_class = UserRegisterForm
	second_form_class = CityForm
	success_url = reverse_lazy('login')

	def get_context_data(self, **kwargs):
		context = super(UserRegister, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context :
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			user = form.save(commit=False)
			user.city = form2.save()
			user.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))