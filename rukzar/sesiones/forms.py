from django import forms
from sesiones.models import sesion

class SesionNuevaForm(forms.ModelForm):
    class Meta:
        model = sesion
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'comentarios': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
