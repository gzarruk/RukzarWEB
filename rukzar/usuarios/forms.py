from django import forms
from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class PerfilUsuarioForm(forms.ModelForm):
    class Meta():
        model = PerfilUsuario
        fields = ('edad','perfil_pic')
