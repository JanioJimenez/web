from django.contrib.auth.forms import UserCreationForm
from django import forms

from apps.usuario.models import User, City

class UserRegisterForm(UserCreationForm, forms.ModelForm):

    class Meta:
        model = User

        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                'age',
                'language',
            ]
        labels = {
                'age' : 'Edad',
                'language' : 'Lenguaje de preferencia',
            }
        widgets = {
            'language' : forms.Select(attrs={'required':'required'}),
        }



class CityForm(forms.ModelForm):

    class Meta:
        model = City

        fields = [
            'name',
            'country',
        ]
        labels = {
            'name' : 'Ciudad',
            'country' : 'Pais',
        }
