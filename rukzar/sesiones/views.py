from django.shortcuts import render
from sesiones.forms import SesionNuevaForm

# Create your views here.
def sesiones_inicio(request):
    context_dict = {'text':'Hola guapo, eres un ', 'number':10}
    return render(request, 'sesiones/sesiones_inicio.html',context_dict)

def sesion_nueva(request):
    form = SesionNuevaForm()

    if request.method=='POST':
        form = SesionNuevaForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return sesiones_inicio(request)
        else:
            print('ERROR: FORMULARIO INVALIDO')

    return render(request,'sesiones/crear_sesion.html',{'form':form})

def other(request):
    return render(request, 'sesiones/other.html')
