from django import forms
from django.db import models

from usuario.models import Usuario

from .models import Consulta
from medicamento.models import Medicamento


class ConsultaForm(forms.ModelForm):
    medico = forms.ModelChoiceField(label='Médico na consulta *', queryset=Usuario.medicos.all())
    medicamentos = forms.ModelMultipleChoiceField(label='Medicamento(s)', queryset=Medicamento.medicamentos_ativos.all(), required=False)

    class Meta:
        model = Consulta
        fields = ['medico', 'unidade', 'paciente_triagem', 'prescricao', 'medicamentos']
    


