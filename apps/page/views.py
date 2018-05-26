from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.urls import reverse

from django.contrib.auth.models import User
from django.views.generic import CreateView

from apps.page.models import Idiom, Info
from apps.usuario.models import Code, User as Usuario
from apps.usuario.forms import UserRegisterForm, CityForm, UserCompleteForm
from apps.compiler.views import compile

from social_django.models import UserSocialAuth

def home(request, idiom="es"):
	language = Idiom.objects.filter(min_name=idiom).first()

	if language:
		idioms = Idiom.objects.all()
		context = {"language" : language, "idioms":idioms}
		# return HttpResponse(idiom.info.title);
		return render(request, 'page/home.html', context)
	else:
		return HttpResponse("El idioma no fue encontrado");

def redirect(request, idiom="es", pagename="home"):
	language = Idiom.objects.filter(min_name=idiom).first()

	if language:
		idioms = Idiom.objects.all()
		context = {"language" : language, "idioms":idioms}

		if pagename == 'compile':
			return compile(request, context)
		if pagename == 'community':
			context.setdefault("codes", Code.objects.order_by('-creation_date'))

		if request.user.age:
			return render(request, 'page/'+pagename+'.html', context)
		else:
			return HttpResponseRedirect(pagename+'/complete-register')
			# return HttpResponseRedirect(reverse('page:complete-register'))
			# return render(request, 'user/complete-register.html', context)

	else:
		return HttpResponse("El idioma no fue encontrado");

def user_complete_register(request, idiom="es", pagename="home"):
	language = Idiom.objects.filter(min_name=idiom).first()

	user = Usuario.objects.get(id=request.user.id)
	if language:
		idioms = Idiom.objects.all()

		if request.method == 'POST':

			form = UserCompleteForm(request.POST, instance=user)
			form2 = CityForm(request.POST)

			print('form.is_valid()------->',form.is_valid())
			print('form2.is_valid()------->',form2.is_valid())
			if form.is_valid() and form2.is_valid():
				# user = form.save(commit=False)
				print('--------> Es valido se guardaran los cambios')
				social_user = UserSocialAuth.objects.get(user_id=request.user.id)
				if social_user:
					provider = social_user.provider
				else:
					provider = 'none'
				user.provider = provider
				user.city = form2.save()
				user.save()

			return HttpResponseRedirect(reverse_lazy('page:redirect',  args=[idiom, pagename]))
		else:
			form = UserCompleteForm(instance=user)
			form2 = CityForm()

		return render(request, 'user/complete-register.html', {"language" : language, "idioms":idioms, 'form':form, 'form2':form2})
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
