from django import forms
from django.db import models

from usuario.models import Usuario
from .models import Evento


class EventoForm(forms.ModelForm):
    coordenador = forms.ModelChoiceField(label='Coordenador responsável *', queryset=Usuario.coordenadores.all())
    coordenador_suplente = forms.ModelChoiceField(label='Coordenador suplente', queryset=Usuario.coordenadores.all(), required=False)

    class Meta:
        model = Evento
        fields = ['nome', 'tipo', 'instituicao', 'coordenador', 'coordenador_suplente', 'email', 'data_inicio', 'data_limite_trabalhos', 'modelo_artigo', 'arquivo_modelo', 'is_active']


class BuscaEventoForm(forms.Form):        
    pesquisa = forms.CharField(label='Pesquisa livre', required=False)
    
    