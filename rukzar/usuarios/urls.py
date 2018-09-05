from django.urls import path
from usuarios import views

# Template tagging

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('usuario_login/',views.usuario_login,name='usuario_login'),
]
