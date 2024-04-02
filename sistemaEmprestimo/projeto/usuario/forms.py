from django import forms
from .models import Usuario


class UsuarioRegisterForm(forms.ModelForm):
    TIPOS_USUARIOS = (
        ('USUÁRIO', 'Usuário' ),
    )
    
    tipo = forms.ChoiceField(label='Tipo',choices=TIPOS_USUARIOS)
    nome = forms.CharField(label='Nome completo *' , help_text='Campo obrigatório como todos os que tiverem *' )
    apelido = forms.CharField(label='Apelido', max_length=100, required=False)
    celular = forms.CharField(label='Celular * ', help_text="Com WhattsApp")
    email = forms.EmailField(label= 'Email *', max_length=100)
    password = forms.CharField(label= "Senha", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['tipo','nome','apelido','celular','email','password']