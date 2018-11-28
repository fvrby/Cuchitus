from django import forms
from .models import Cliente, Post
from django.core.exceptions import ValidationError


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('correo', 'run', 'nombreCompleto', 'telefono',)
