from django.shortcuts import render
from usuarios.forms import UsuarioForm, PerfilUsuarioForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def usuario_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('sesiones_inicio'))

@login_required
def especial(request):
    return HttpResponse('Sesión Activa!')

def registro(request):

    registrado = False

    if request.method == 'POST':
        usuario_form = UsuarioForm(data=request.POST)
        perfil_form = PerfilUsuarioForm(data=request.POST)

        if usuario_form.is_valid() and perfil_form.is_valid():

            usuario = usuario_form.save()
            usuario.set_password(usuario.password)
            usuario.save()

            perfil = perfil_form.save(commit=False)
            perfil.usuario = usuario

            if 'perfil_pic' in request.FILES:
                perfil.perfil_pic = request.FILES['perfil_pic']

            perfil.save()

            registrado = True
        else:
            print(usuario_form.errors,perfil_form.errors)
    else:
        usuario_form = UsuarioForm()
        perfil_form = PerfilUsuarioForm()

    return render(request,'usuarios/registro.html',
                            {'usuario_form': usuario_form,
                             'perfil_form': perfil_form,
                             'registrado': registrado})


def usuario_login(request):

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')

        usuario = authenticate(username=usuario,password=contraseña)

        if usuario:
            if usuario.is_active:
                login(request,usuario)
                return HttpResponseRedirect(reverse('sesiones_inicio'))

            else:
                return HttpResponse('La cuenta no está activa')
        else:
            print('Alguien intento ingresar y fallo')
            print('Usuario: {} y contraseña: {}'.format(usuario,contraseña))
            return HttpResponse('Datos de registro incorrectos')

    else:
        return render(request,'usuarios/login.html',{})
