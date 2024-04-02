from django import forms
from django.db import models

from usuario.models import Usuario
from paciente.models import Paciente

from .models import Triagem


class TriagemFormCreate(forms.ModelForm):
    responsavel = forms.ModelChoiceField(label='Responsável pela triagem *', queryset=Usuario.tecnicos_enfermeiros.all())
    paciente2 = forms.ModelChoiceField(label='Paciente *', queryset=Paciente.pacientes_ativos.all())

    class Meta:
        model = Triagem
        fields = ['responsavel', 'unidade', 'paciente2', 'altura', 'peso',
              'tem_febre', 'tem_dor_cabeca', 'tem_secrecao_espirros', 'tem_irritacao_garganta',
              'tem_tosse', 'tem_dificuldade_respiratoria', 'tem_dores_corpo', 'tem_diarreia',
              'viajou', 'contatou']
    


class TriagemFormUpdate(forms.ModelForm):
    responsavel = forms.ModelChoiceField(label='Responsável pela triagem *', queryset=Usuario.tecnicos_enfermeiros.all())
    

    class Meta:
        model = Triagem
        fields = ['responsavel', 'unidade', 'altura', 'peso']

