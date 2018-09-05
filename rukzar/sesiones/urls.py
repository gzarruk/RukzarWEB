from django.urls import path
from sesiones import views

# Template tagging

app_name = 'sesiones'

urlpatterns = [
    path('', views.sesiones_inicio, name='sesiones_inicio'),
    path('nueva/', views.sesion_nueva, name='SesionNueva'),
    path('other/', views.other, name='other'),
]
