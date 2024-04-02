from django import forms
from django.db import models

from usuario.models import Usuario

from .models import Emprestimo


class EmprestimoForm(forms.ModelForm):
    locador = forms.ModelChoiceField(label='Locador *', queryset=Usuario.usuarios.all())

    class Meta:
        model = Emprestimo
        fields = ['locador', 'objeto', 'data_emprestimo', 'em_emprestimo']
    
