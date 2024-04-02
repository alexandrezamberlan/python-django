from django import forms
from django.db import models

class BuscaMedicamentoForm(forms.Form):    
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS_TARJAS = (
        (None, '-----'),
        ('BRANCA', 'Branca'),
        ('AMARELA', 'Amarela'),
        ('VERMELHA', 'Vermelha'),
        ('PRETA', 'Preta'),
    )
    TIPOS_MEDICAMENTOS = (
        (None, '-----'),
        ('CÁPSULA', 'Cápsula'),
        ('COMPRIMIDO', 'Comprimido'),
        ('LÍQUIDO', 'Líquido')        
    )
    tipo = forms.ChoiceField(label='Tipo Medicmaneto', choices=TIPOS_MEDICAMENTOS, required=False)
    tarja = forms.ChoiceField(label='Tarja do Medicamento', choices=TIPOS_TARJAS, required=False)
    