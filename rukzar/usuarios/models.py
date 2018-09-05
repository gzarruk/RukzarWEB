from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional entries to User model

    edad = models.IntegerField(blank=True,
                                validators=[
                                        MaxValueValidator(100),
                                        MinValueValidator(18)
                                            ])
    perfil_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.usuario.username
