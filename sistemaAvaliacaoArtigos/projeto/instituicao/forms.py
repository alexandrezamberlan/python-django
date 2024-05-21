from django import forms
from django.db import models

class BuscaInstituicaoForm(forms.Form):    
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    nome  = forms.CharField(label='Nome da instituição', required=False)
    sigla = forms.CharField(label='Sigla da instituição', required=False)
    