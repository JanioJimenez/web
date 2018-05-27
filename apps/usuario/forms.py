from django.contrib.auth.forms import UserCreationForm
from django import forms

from apps.usuario.models import User, City, Code

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

class UserCompleteForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
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
            # 'city' : forms.Select(attrs={'required':'required'}),
            # 'city' : forms.CharField(),
        }

class CodeForm(forms.ModelForm):

    class Meta:
        model = Code

        fields = [
            'name',
            'code',
            'description',
            'compilations',
            'user',
            # 'creation_date',
        ]
        labels = {
            'name' : 'Nombre del código',
            'code' : 'Codigo',
            'description' : 'Descripcion',
            'compilations' : 'Número de compilaciones',
            # 'creation_date' : 'Fecha Creacion',
        }

class UserUpdateForm(forms.ModelForm):

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

class UserUpdatePasswordForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
                'password',
            ]
        # labels = {
        #
        #     }
        # widgets = {
        #
        # }
