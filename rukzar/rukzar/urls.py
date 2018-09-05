"""rukzar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from django.conf import settings
from sesiones import views
from usuarios import views as usuarios_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sesiones/', include('sesiones.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('', views.sesiones_inicio, name='sesiones_inicio'),
    path('logout/',usuarios_views.usuario_logout,name='logout'),
    path('especial/',usuarios_views.especial,name='especial')
]
