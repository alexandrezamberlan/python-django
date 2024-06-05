from django import forms
from django.db import models

class BuscaInstituicaoForm(forms.Form):        
    pesquisa = forms.CharField(label='Pesquisa livre', required=False)
    
    